import argparse
import subprocess
import platform
from core_lib.Logger import Logger

logger = Logger()

ap = argparse.ArgumentParser()
ap.add_argument(
    "-t",
    "--tags",
    action="append",
    help="Enter tag you want to run test, to run multiple tags call -t tag_1 -t tag_2 -t tag_3",
)

ap.add_argument("-n", "--number-of-threads", type=int, help="Number of tests run parallel")

ap.add_argument("-l", "--log-level", default="INFO", help="Set debug level: DEBUG, INFO")

ap.add_argument(
    "-d", "--report-directory", default="allure-report", help="Set Report Directory, default: allure-report"
)

ap.add_argument("--show-report", default=False, action=argparse.BooleanOptionalAction, help="Show Report After running")

ap.add_argument(
    "--install-libraries", default=True, action=argparse.BooleanOptionalAction, help="Install Required Libraries"
)

args = vars(ap.parse_args())
tags = args.get("tags")
nof_threads = args.get("number_of_threads")
log_level = args.get("log_level").upper()
report_dir = args.get("report_directory")
install_req_libs = args.get("install_libraries")
show_report = args.get("show_report")

condition = platform.system().lower() in ["linux", "darwin"]
_python = "python3" if condition else "python"
_pytest = f"{_python} -m pytest"

base_command = f"""{_pytest} --disable-pytest-warnings --alluredir "{report_dir}" """
if nof_threads:
    base_command += f"-n {nof_threads} "

base_command += f"""--log-cli-level {log_level} """

if tags:
    _tags = ""
    for tag in tags:
        _tags += f"--tags {tag} "
    base_command += _tags.strip()
if install_req_libs:
    logger.info_in_box("Install Required Libraries")
    subprocess.run("npm install -g allure-commandline", shell=True)
    subprocess.run(f"{_python} -m pip install --upgrade pip", shell=True)
    subprocess.run(f"{_python} -m pip install -r requirements.txt", shell=True)

logger.info_in_box("Cleanup report directory")
subprocess.run("allure generate --clean --output allure-report", shell=True)

logger.info_in_box("Update test steps and scenarios")
subprocess.run(f"{_python} core_lib/update_test_steps_and_scenarios.py", shell=True)

logger.info_in_box("Reformat Code")
subprocess.run("black --check .", shell=True)
subprocess.run("black .", shell=True)
logger.info_in_box("Check Linting")
subprocess.run("flake8", shell=True)

logger.info_in_box("Execute command")
logger.info(base_command)
sub_process = subprocess.run(base_command, shell=True)
if show_report:
    logger.info_in_box("Show Report")
    subprocess.run(f"allure serve {report_dir}", shell=True)
