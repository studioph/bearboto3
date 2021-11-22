import argparse
import json
from pathlib import Path

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

classes_file = here.joinpath(f"{args.service}_classes.json")
with classes_file.open("r") as file:
    mappings = json.load(file)

client_base_types = ["Waiter", "Paginator", "BaseClient"]
resource_base_types = ["ServiceResource", "ResourceCollection"]
client_stubs = [
    mapping["stub_class"]
    for mapping in mappings
    if mapping["base_class"] in client_base_types
]
resource_stubs = [
    mapping["stub_class"]
    for mapping in mappings
    if mapping["base_class"] in resource_base_types
]

template_file = here.joinpath("template.py")
with template_file.open("r") as file:
    template = file.read()

client_stubs_str = ", ".join(client_stubs)
resource_stubs_str = ", ".join(resource_stubs)

template = template.replace("{service}", args.service)
template = template.replace("{client_types}", client_stubs_str)
template = template.replace("{resource_types}", resource_stubs_str)

annotation_template = '{stub_type} = Annotated[{base_type}, IsAttr["__class__", IsAttr["__name__", IsEqual["{boto_type}"]]]]'

annotations = [
    annotation_template.replace("{stub_type}", mapping["stub_class"])
    .replace("{base_type}", mapping["base_class"])
    .replace("{boto_type}", mapping["boto_class"])
    for mapping in mappings
]

annotations_str = "\n    ".join(annotations)

template = template.replace("{type_annotations}", annotations_str)

output_file = here.parent.joinpath("bearboto3").joinpath(f"{args.service}.py")
with output_file.open("w") as file:
    file.write(template)
