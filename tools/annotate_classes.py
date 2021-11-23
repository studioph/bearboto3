import argparse
import json
import operator
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
    # required=True,
    help='Service to load {service}_classes.json and output "bearboto3/{service}.py"',
)
args = parser.parse_args()

here = Path(__file__).parent

classes_file = here.joinpath(f"{args.service}_classes.json")
with classes_file.open("r") as file:
    entries = json.load(file)
entries.sort(key=operator.itemgetter("stub_class"))

client_base_types = ["Waiter", "Paginator", "BaseClient"]
resource_base_types = ["ServiceResource", "ResourceCollection"]

client_types = [
    entry["stub_class"] for entry in entries if entry["base_class"] in client_base_types
]
resource_types = [
    entry["stub_class"]
    for entry in entries
    if entry["base_class"] in resource_base_types
]

templates_folder = here.parent.joinpath("templates")
env = Environment(loader=FileSystemLoader(templates_folder))
template_file = env.get_template("annotations.py.j2")

output_file = here.parent.joinpath("bearboto3").joinpath(f"{args.service}.py")
with output_file.open("w") as file:
    template_file.stream(
        annotations=entries,
        service=args.service,
        client_types=client_types,
        resource_types=resource_types,
    ).dump(file)
black.format_file_in_place(
    output_file, fast=False, write_back=black.WriteBack.YES, mode=black.FileMode()
)
