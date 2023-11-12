import yaml
import json
import functools
import operator
from genson import SchemaBuilder


def read_yaml(file):
    with open(file, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def write_to_yaml(file, dict_content):
    with open(file, "w") as f:
        return yaml.dump(dict_content, f)


def read_json(file):
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_json_schema(json_data):
    builder = SchemaBuilder()
    builder.add_object(json_data)
    schema = builder.to_schema()
    return schema


def write_file(file, data):
    with open(file, "w") as f:
        return f.write(data)


def get_from_dict(data_dict, keys: str):
    map_list = keys.split(".")
    try:
        return functools.reduce(operator.getitem, map_list, data_dict)
    except Exception:
        return keys
