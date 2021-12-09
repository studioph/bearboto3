import argparse
import inspect
import json
import os
from pathlib import Path

import boto3
import botocore
from botocore import xform_name

parser = argparse.ArgumentParser(
    description="Gathers data needed for annotating classes and generating test cases by parsing the boto JSON schema."
)
parser.add_argument(
    "--service",
    type=str,
    required=True,
    help="Service name (lowercase) to annotate classes for",
)
args = parser.parse_args()

UTF_8 = "utf-8"
DATA_FOLDER = "data"
COLLECTION_SUFFIX = "Collection"
COLLECTIONS_KEY = "hasMany"
RESOURCE_BASE_CLASS = "ServiceResource"
COLLECTION_BASE_CLASS = "ResourceCollection"
PAGINATOR_BASE_CLASS = "Paginator"
WAITER_BASE_CLASS = "Waiter"
CLIENT_BASE_CLASS = "BaseClient"
RESOURCES_FILE_NAME = "resources-1.json"
PAGINATORS_FILE_NAME = "paginators-1.json"
WAITERS_FILE_NAME = "waiters-2.json"
READ = "r"
WRITE = "w"
SERVICE_NAME_PASCAL = args.service.upper()
SERVICE_NAME_SNAKE = xform_name(args.service)
CONSTRUCTOR_ARGS_KEY = "identifiers"


def get_latest_version(folder: Path) -> Path:
    folders = os.listdir(folder.resolve())
    latest_version = max(folders)
    return folder.joinpath(latest_version)


def get_waiters(folder: Path) -> list[dict[str, str]]:
    waiters_file = folder.joinpath(WAITERS_FILE_NAME)
    with waiters_file.open(READ, encoding=UTF_8) as fp:
        waiters_json = json.load(fp)

    return [
        {
            "stub_class": f"{waiter}{WAITER_BASE_CLASS}",
            "boto_class": f"{SERVICE_NAME_PASCAL}.{WAITER_BASE_CLASS}.{waiter}",
            "base_class": WAITER_BASE_CLASS,
            "fixture_name": f"gen_{xform_name(waiter)}_waiter",
            "snake_name": xform_name(waiter),
        }
        for waiter in waiters_json["waiters"]
    ]


def get_paginators(folder: Path) -> list[dict[str, str]]:
    paginators_file = folder.joinpath(PAGINATORS_FILE_NAME)
    with paginators_file.open(READ, encoding=UTF_8) as fp:
        paginators_json = json.load(fp)

    return [
        {
            "stub_class": f"{paginator}{PAGINATOR_BASE_CLASS}",
            "boto_class": f"{SERVICE_NAME_PASCAL}.{PAGINATOR_BASE_CLASS}.{paginator}",
            "base_class": PAGINATOR_BASE_CLASS,
            "fixture_name": f"gen_{xform_name(paginator)}_paginator",
            "snake_name": xform_name(paginator),
        }
        for paginator in paginators_json["pagination"]
    ]


def get_collections(
    parent_key: str, parent_node: dict, parent_item: dict[str, str]
) -> list[dict[str, str]]:
    return [
        {
            "stub_class": f"{parent_key}{collection}{COLLECTION_SUFFIX}",
            "boto_class": f"{SERVICE_NAME_SNAKE}.{parent_key}.{xform_name(collection)}{COLLECTION_SUFFIX}",
            "base_class": COLLECTION_BASE_CLASS,
            "fixture_name": f"gen_{xform_name(collection)}_collection",
            "snake_name": xform_name(collection),
            "parent_fixture_name": parent_item["fixture_name"],
        }
        for collection in parent_node["hasMany"]
    ]


def get_resource(key: str, val: dict) -> tuple:
    num_constructor_args = (
        len(val[CONSTRUCTOR_ARGS_KEY]) if CONSTRUCTOR_ARGS_KEY in val else 0
    )

    item = {
        "stub_class": key,
        "boto_class": f"{SERVICE_NAME_SNAKE}.{key}",
        "base_class": RESOURCE_BASE_CLASS,
        "fixture_name": f"gen_{xform_name(key)}",
        "snake_name": xform_name(key),
        "constructor_args": ",".join(
            ["random_str()" for _ in range(num_constructor_args)]
        ),
    }

    collections = []
    if COLLECTIONS_KEY in val:
        collections = get_collections(key, val, item)

    return item, collections


def get_resources(folder: Path) -> dict:
    resources_file = folder.joinpath(RESOURCES_FILE_NAME)
    with resources_file.open(READ, encoding=UTF_8) as fp:
        resources_json = json.load(fp)

    result = {
        "service_resource": {
            "stub_class": f"{SERVICE_NAME_PASCAL}{RESOURCE_BASE_CLASS}",
            "boto_class": f"{SERVICE_NAME_SNAKE}.{RESOURCE_BASE_CLASS}",
            "base_class": RESOURCE_BASE_CLASS,
            "fixture_name": f"gen_{SERVICE_NAME_SNAKE}_resource",
            "snake_name": f"{SERVICE_NAME_SNAKE}_resource",
        },
        "collections": [],
        "resources": [],
    }

    if COLLECTIONS_KEY in resources_json["service"]:
        result["collections"] = get_collections(
            RESOURCE_BASE_CLASS, resources_json["service"], result["service_resource"]
        )

    for key, val in resources_json["resources"].items():
        item, collections = get_resource(key, val)
        result["resources"].append(item)
        result["collections"] += collections

    return result


here = Path(__file__).parent
boto3_path = Path(inspect.getfile(boto3)).parent
botocore_path = Path(inspect.getfile(botocore)).parent


resource_data_folder = boto3_path.joinpath(DATA_FOLDER).joinpath(args.service)
client_data_folder = botocore_path.joinpath(DATA_FOLDER).joinpath(args.service)


has_resources = resource_data_folder.exists()
data = {
    "client": {
        "stub_class": f"{SERVICE_NAME_PASCAL}Client",
        "boto_class": SERVICE_NAME_PASCAL,
        "base_class": CLIENT_BASE_CLASS,
        "fixture_name": f"gen_{SERVICE_NAME_SNAKE}_client",
        "snake_name": f"{SERVICE_NAME_SNAKE}_client",
    },
    "paginators": [],
    "waiters": [],
}


schema_folder = get_latest_version(client_data_folder)

data["paginators"] += get_paginators(schema_folder)
data["waiters"] += get_waiters(schema_folder)

if has_resources:
    schema_folder = get_latest_version(resource_data_folder)
    data |= get_resources(schema_folder)

output_folder = here.parent.joinpath("data")
output_folder.mkdir(parents=True, exist_ok=True)
output_file = output_folder.joinpath(f"{args.service}_data.json")
with output_file.open(WRITE, encoding=UTF_8) as fp:
    json.dump(data, fp)
