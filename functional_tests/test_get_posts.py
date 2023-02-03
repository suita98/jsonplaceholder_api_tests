import pytest
from random import choice

from api_client.jsonplaceholder_api import ApiClient
from framework.constants import TOTAL_POSTS_NUMBER, USER_IDS
from framework.checker import check_list_items_count, check_post_by


api = ApiClient()


def test_get_total_posts_count():
    response = api.get_posts()
    check_list_items_count(response.json(), TOTAL_POSTS_NUMBER)


@pytest.mark.parametrize('parameter, values', [('userId', USER_IDS)])
def test_get_posts_by(parameter, values):
    expected_value = choice(values)
    params = {parameter: expected_value}
    response = api.get_posts(params=params)
    check_post_by(parameter, expected_value, response.json())
