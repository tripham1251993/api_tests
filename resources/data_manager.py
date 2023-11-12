import os
import sys

dir_name = os.path.dirname(__file__).replace("resources", "")
sys.path.append(dir_name)
from core_lib.utilities import read_yaml, get_from_dict, generate_json_schema

dir_name = os.path.dirname(__file__).replace("resources", "")
request_files = []
request_dir = os.path.join(dir_name, "data", "request")
schema_dir = os.path.join(dir_name, "data", "schema")


def __get_files(folder):
    result = []
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            result.append(file_path)
    return result


request_files = __get_files(request_dir)
schema_files = __get_files(schema_dir)

REQUEST_DATA = {}
for file in request_files:
    REQUEST_DATA.update(read_yaml(file))

SCHEMA_DATA = {}
for file in schema_files:
    file_name = os.path.basename(file)
    file_name = os.path.splitext(file_name)[0]
    SCHEMA_DATA[file_name] = read_yaml(file)


def get_request_data(key):
    """Get request data, if the key not found return key

    Args:
        key (str): key should in format "key" or "parent.child.child"

    Returns:
        any: (str, list, dict, int)
    """
    return get_from_dict(REQUEST_DATA, key)


def get_schema_data(key):
    """Get Schema data, if the key not found return key

    Args:
        key (str): key should in format "key" or "parent.child.child"

    Returns:
        any: (str, list, dict, int)
    """
    try:
        raw_data = get_from_dict(SCHEMA_DATA, key)
        schema = generate_json_schema(raw_data)
        return schema
    except Exception:
        return None
