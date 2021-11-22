import argparse
import json

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

classes_file = f"{args.service}_classes.json"
with open(classes_file, "r") as file:
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

template_file = "template.py"
with open(template_file, "r") as file:
    template = file.read()

client_stubs_str = ",".join(client_base_types)
resource_stubs_str = ",".join(resource_base_types)

template = template.replace("{service}", args.service)
template = template.replace("{client_types}", client_stubs_str)
template = template.replace("{resource_types}", resource_stubs_str)

annotation_template = '{stub_type} = Annotated[{base_type}, IsAttr["__class__", IsAttr["__name__", IsEqual[{boto_type}]]]]'

annotations = [
    annotation_template.replace("{stub_type}", mapping["stub_class"])
    .replace("{base_type}", mapping["base_class"])
    .replace("{boto_type}", mapping["boto_class"])
    for mapping in mappings
]

annotations_str = "\n".join(annotations)

template = template.replace("{type_annotations}", annotations_str)

output_file = f"bearboto3/{args.service}.py"
with open(output_file, "w") as file:
    file.write(template)
