import os
import sys

dir_name = os.path.dirname(__file__).replace("core_lib", "")
sys.path.append(dir_name)

api_data_files = []
api_data_dir = os.path.join(dir_name, "tests", "api")

api_features = []


def get_scenarios(folder):
    result = "scenarios(\n"
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            _, extension = os.path.splitext(file)
            if extension == ".feature":
                result += f"""\t"features/{file}",\n"""
    result += ")\n"
    return result


def get_imports(folder):
    result = "from pytest_bdd import scenarios"
    sub_folder = "api" if "api" in folder else "e2e"
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            filename, _ = os.path.splitext(file)
            if filename != "__init__":
                result += f"""\nfrom tests.{sub_folder}.steps_def.{filename} import *"""
    return result + "\n\n"


api_scenarios = get_scenarios(os.path.join(api_data_dir, "features"))
api_import = get_imports(os.path.join(api_data_dir, "steps_def"))

if "features" in api_scenarios:
    with open(os.path.join(api_data_dir, "test_steps_and_scenarios.py"), "w", encoding="utf-8") as f:
        f.write(api_import + api_scenarios)
else:
    path = os.path.join(api_data_dir, "test_steps_and_scenarios.py")
    if os.path.exists(path):
        os.remove(path)
