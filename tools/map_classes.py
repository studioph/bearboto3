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

here = Path(__file__).parent


boto3_path = Path(inspect.getfile(boto3)).parent
botocore_path = Path(inspect.getfile(botocore)).parent

data_folder = "data"
resource_data_folder = boto3_path.joinpath(data_folder)
client_data_folder = botocore_path.joinpath(data_folder)

collection_suffix = "Collection"
collections_key = "hasMany"
resource_base = "ServiceResource"
collections_base = "ResourceCollection"
paginator_base = "Paginator"
waiter_base = "Waiter"
client_base = "BaseClient"


def get_latest_version(folder: Path) -> str:
    return max(os.listdir(folder.resolve()))


def get_service_classes(service: str) -> dict:
    resource_prefix = service
    client_name = service.upper()
    other_prefix = client_name

    return get_client_classes(service, other_prefix) | get_resource_classes(
        service, resource_prefix, other_prefix
    )


def get_resource_classes(service: str, resource_prefix: str, other_prefix: str) -> dict:
    service_folder = resource_data_folder.joinpath(service)
    latest = get_latest_version(service_folder)
    resource_file = service_folder.joinpath(latest).joinpath("resources-1.json")

    classes = {}
    if resource_file.exists():
        with resource_file.open("r") as file:
            resource_data = json.load(file)

        classes = get_resources(resource_prefix, other_prefix, resource_data)
        classes["collections"] = get_collections(resource_prefix, resource_data)
    return classes


def get_resources(resource_prefix: str, other_prefix: str, model: dict) -> dict:
    # Start with service resource itself
    classes = {
        "service_resource": {
            "stub_class": f"{other_prefix}{resource_base}",
            "boto_class": f"{resource_prefix}.{resource_base}",
            "base_class": resource_base,
        }
    }
    # Map each type under the "resources" key
    classes["resources"] = [
        {
            "stub_class": resource,
            "boto_class": f"{resource_prefix}.{resource}",
            "base_class": resource_base,
            "snake_name": xform_name(resource),
        }
        for resource in list(model["resources"].keys())
    ]
    return classes


def get_collections(service: str, model: dict) -> list[dict[str, str]]:
    # Collections in the service resource
    classes = (
        [
            {
                "stub_class": f"{resource_base}{item}{collection_suffix}",
                "boto_class": f"{service}.{xform_name(item)}{collection_suffix}",
                "base_class": collections_base,
                "field": xform_name(item),
                "fixture": f"{service}_resource",
            }
            for item in model["service"][collections_key]
        ]
        if collections_key in model["service"]
        else []
    )
    # Collections in other resources
    for resource, definition in model["resources"].items():
        if collections_key in definition:
            classes += [
                {
                    "stub_class": f"{resource}{item}{collection_suffix}",
                    "boto_class": f"{service}.{resource}.{xform_name(item)}{collection_suffix}",
                    "base_class": collections_base,
                    "field": xform_name(item),
                    "fixture": f"gen_{xform_name(item[:-1])}",
                }
                for item in definition[collections_key]
            ]
    return classes


def get_client_classes(service: str, prefix: str) -> dict:
    service_folder = client_data_folder.joinpath(service)
    latest = get_latest_version(service_folder)
    waiters_file = service_folder.joinpath(latest).joinpath("waiters-2.json")
    paginators_file = service_folder.joinpath(latest).joinpath("paginators-1.json")

    with waiters_file.open("r") as file:
        waiter_data = json.load(file)
    with paginators_file.open("r") as file:
        paginator_data = json.load(file)

    classes = {
        "client": {
            "stub_class": f"{prefix}Client",
            "boto_class": prefix,
            "base_class": client_base,
        }
    }

    classes["paginators"] = get_paginators(prefix, paginator_data)
    classes["waiters"] = get_waiters(prefix, waiter_data)
    return classes


def get_waiters(prefix: str, model: dict) -> list[dict[str, str]]:
    return [
        {
            "stub_class": f"{waiter}{waiter_base}",
            "boto_class": f"{prefix}.{waiter_base}.{waiter}",
            "base_class": waiter_base,
            "snake_name": xform_name(waiter),
        }
        for waiter in model["waiters"]
    ]


def get_paginators(prefix: str, model: dict) -> list[dict[str, str]]:
    return [
        {
            "stub_class": f"{paginator}{paginator_base}",
            "boto_class": f"{prefix}.{paginator_base}.{paginator}",
            "base_class": paginator_base,
            "snake_name": xform_name(paginator),
        }
        for paginator in model["pagination"]
    ]


classes = get_service_classes(args.service)

output_folder = here.parent.joinpath("data")
output_folder.mkdir(parents=True, exist_ok=True)
output_file = output_folder.joinpath(f"{args.service}_data.json")
with output_file.open("w") as fp:
    json.dump(classes, fp)
