from pytest_bdd import given, when, then, parsers
from pom.api.ApiModel import ApiModel
import pytest
import jsonschema

RESPONSE_DATA = {}


def validate_schema(actual_data, schema):
    try:
        jsonschema.validate(instance=actual_data, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        pytest.fail(f"{actual_data}\ndoes not match schema: {schema}\nError: {e}")


@when(parsers.parse('''User call auth api with credential "{credential}"'''))
def users_auth(api_model: ApiModel, get_request_data, credential):
    data = get_request_data(credential)
    resp = api_model.get_access_token(payload=data)
    RESPONSE_DATA["get_access_token"] = resp


@then(parsers.parse('''Response code should be "{response_code}"'''))
def verify_auth_response_code(get_dict_data, response_code):
    actual = get_dict_data(RESPONSE_DATA, "get_access_token.code")
    assert int(actual) == int(response_code)


@then(parsers.parse("""Response time should less than "{response_time}"s"""))
def verify_auth_response_time(get_dict_data, response_time):
    actual = get_dict_data(RESPONSE_DATA, "get_access_token.time")
    assert float(actual) < float(response_time)


@then(parsers.parse('''Response should match schema "{schema}"'''))
def verify_auth_response_structure(get_dict_data, get_schema_data, schema):
    schema = get_schema_data(schema)
    actual = get_dict_data(RESPONSE_DATA, "get_access_token.body")
    validate_schema(actual_data=actual, schema=schema)
