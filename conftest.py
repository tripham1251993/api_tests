import pytest

from resources import data_manager
from core_lib.Logger import Logger
from pom.api.ApiModel import ApiModel
import jsonschema


ERROR_STEPS = {}
logger = Logger()


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    for sc_step in scenario.steps:
        if sc_step.name == step.name:
            ERROR_STEPS[f"{feature.name}.{scenario.name}"] = step
            break


def pytest_bdd_after_scenario(request, feature, scenario):
    logger.info("╔═" + "═" * 60)
    logger.info("║ Features: " + feature.name)
    logger.info("║ " + " " * 2 + "Scenario: " + scenario.name)
    for step in scenario.steps:
        if ERROR_STEPS.__contains__(f"{feature.name}.{scenario.name}"):
            if step.name == ERROR_STEPS.get(f"{feature.name}.{scenario.name}").name:
                logger.info("║ " + " " * 4 + "❌ " + f"{step.keyword} " + step.name)
                break
        logger.info("║ " + " " * 4 + "✅ " + f"{step.keyword} " + step.name)
    logger.info("╚═" + "═" * 60)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.markexpr = "not not_in_scope"


def pytest_addoption(parser):
    parser.addoption("--tags", action="append", help="Will filter tests by given tags")
    parser.addoption(
        "--resolution",
        action="store",
        default="1920x1080",
        type=str,
        help="Enter screen size WxH. Ex: 1920x1080, 1366x768, 800x600",
    )


def pytest_collection_modifyitems(config, items):
    raw_tags = config.option.tags
    if raw_tags is not None:
        for item in items:
            item_tags = [marker.name for marker in item.own_markers]
            checks = False
            for tag in item_tags:
                checks = tag in raw_tags
                if checks:
                    break
            if not checks:
                item.add_marker(pytest.mark.not_in_scope)


@pytest.fixture(scope="session", autouse=True)
def get_request_data():
    """Get API request data

    Returns:
        function: get_request_data data by inputing key
    """
    return data_manager.get_request_data


@pytest.fixture(scope="session", autouse=True)
def get_schema_data():
    """Get schema data by inputing schema file name without extension

    Returns:
        function: get_schema_data
    """
    return data_manager.get_schema_data


@pytest.fixture
def get_dict_data():
    return data_manager.get_from_dict


@pytest.fixture
def api_model(get_request_data):
    api_model = ApiModel(base_url=get_request_data("BASE_URL"))
    return api_model
