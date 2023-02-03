from api_client.jsonplaceholder_api import ApiClient
from framework.checker import smoke_checker


api = ApiClient()


@smoke_checker
def test_get_posts():
    response = api.get_posts()
    return response