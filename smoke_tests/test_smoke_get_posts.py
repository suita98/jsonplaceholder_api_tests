from api_client.jsonplaceholder_api import ApiClient
from api_client.schemas import get_posts_response_schema
from framework.checker import smoke_checker


api = ApiClient()


@smoke_checker
def test_get_posts(schema=get_posts_response_schema):
    response = api.get_posts()
    return response, schema