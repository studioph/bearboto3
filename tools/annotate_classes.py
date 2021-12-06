import argparse
import json
from operator import itemgetter
from pathlib import Path

import black
from jinja2 import Environment, FileSystemLoader

parser = argparse.ArgumentParser(
    description="Automatically annotates classes given a class mapping json file"
)
parser.add_argument(
    "--service",
    type=str,
    required=True,
    help='Service to load {service}_classes.json and output "bearboto3/{service}.py"',
)
args = parser.parse_args()

here = Path(__file__).parent

data_folder = here.parent.joinpath("data")
classes_file = data_folder.joinpath(f"{args.service}_data.json")
with classes_file.open("r") as file:
    data = json.load(file)

has_resources = all(i in data for i in ["service_resource", "collections", "resources"])

client_types = sorted(
    [item["stub_class"] for item in data["waiters"]]
    + [item["stub_class"] for item in data["paginators"]]
    + [data["client"]["stub_class"]]
)
if has_resources:
    resource_types = sorted(
        [item["stub_class"] for item in data["resources"]]
        + [item["stub_class"] for item in data["collections"]]
        + [data["service_resource"]["stub_class"]]
    )

templates_folder = here.parent.joinpath("templates")
env = Environment(loader=FileSystemLoader(templates_folder))
template_file = env.get_template("annotations.py.j2")

items = [data["client"], *data["waiters"], *data["paginators"]]
if has_resources:
    items += data["resources"]
    items += data["collections"]
    items.append(data["service_resource"])

output_file = here.parent.joinpath("bearboto3").joinpath(f"{args.service}.py")
with output_file.open("w") as file:
    template_file.stream(
        annotations=sorted(items, key=itemgetter("stub_class")),
        service=args.service,
        client_types=client_types,
        resource_types=resource_types,
    ).dump(file)
black.format_file_in_place(
    output_file, fast=False, write_back=black.WriteBack.YES, mode=black.FileMode()
)
