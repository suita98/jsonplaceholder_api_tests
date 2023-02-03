from jsonschema import validate
from hamcrest import assert_that, has_length, only_contains


def smoke_checker(func):
    def wrapper_smoke_checker(*args, **kwargs):
        response, schema = func(*args, **kwargs)
        assert response.status_code == 200
        validate(instance=response.json(), schema=schema)
    return wrapper_smoke_checker


def check_list_items_count(response, expected_count):
    assert_that(response, has_length(expected_count))


def check_post_by(parameter, expected_value, posts):
    actual_values = []
    for post in posts:
        actual_values.append(post[parameter])
    assert_that(actual_values, only_contains(expected_value))
