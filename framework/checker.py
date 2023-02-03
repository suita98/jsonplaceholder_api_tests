from jsonschema import validate
from api_client.schemas import get_posts_response_schema


def smoke_checker(func):
    def wrapper_smoke_checker(*args, **kwargs):
        response = func(*args, **kwargs)
        assert response.status_code == 200
        validate(instance=response.json(), schema=get_posts_response_schema)
    return wrapper_smoke_checker


def check_list_items_count(response_list, expected_count):
    assert len(response_list) == expected_count
