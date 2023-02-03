from api_client.jsonplaceholder_api import ApiClient
from framework.constants import TOTAL_POSTS_NUMBER
from framework.checker import check_list_items_count


api = ApiClient()


def test_get_total_posts_count():
    response = api.get_posts()
    check_list_items_count(response.json(), TOTAL_POSTS_NUMBER)
