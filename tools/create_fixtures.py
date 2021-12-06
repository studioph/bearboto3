import argparse
import json
from pathlib import Path

import black
from jinja2 import Environment, FileSystemLoader

parser = argparse.ArgumentParser()
parser.add_argument(
    "--service",
    type=str,
    required=True,
    help="Service to load classes from and create test fixtures for",
)
args = parser.parse_args()

here = Path(__file__).parent

data_folder = here.parent.joinpath("data")
data_file = data_folder.joinpath(f"{args.service}_data.json")
with data_file.open("r") as file:
    data = json.load(file)

templates_folder = here.parent.joinpath("templates")
env = Environment(loader=FileSystemLoader(templates_folder))
template = env.get_template("fixtures.py.j2")


output_folder = here.parent.joinpath("tests").joinpath(args.service)
output_folder.mkdir(parents=True, exist_ok=True)
output_file = output_folder.joinpath(f"{args.service}_fixtures.py")


with output_file.open("w") as fp:
    template.stream(
        service=args.service,
        waiters=data["waiters"],
        paginators=data["paginators"],
        collections=data["collections"],
        resources=data["resources"],
    ).dump(fp)

black.format_file_in_place(
    output_file, fast=False, write_back=black.WriteBack.YES, mode=black.FileMode()
)
