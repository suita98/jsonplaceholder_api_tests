import pytest
from random import choice

from api_client.jsonplaceholder_api import ApiClient
from framework.constants import TOTAL_POSTS_NUMBER, POST_TITLES
from framework.checker import check_list_items_count, check_post_by


api = ApiClient()


def test_get_total_posts_count():
    # TOTAL_POSTS_NUMBER should be replaced with number of posts received from DB
    
    response = api.get_posts()
    check_list_items_count(response.json(), TOTAL_POSTS_NUMBER)


@pytest.mark.parametrize('parameter, values',
                        [('userId', list(range(1, 10))), ('id', list(range(1, 100))), ('title', POST_TITLES)])
def test_get_posts_by(parameter, values):
    expected_value = choice(values)
    params = {parameter: expected_value}
    response = api.get_posts(params=params)
    check_post_by(parameter, expected_value, response.json())


def test_get_posts_by_all_existing_parameters():
    pass


def test_get_posts_by_not_existing_parameter():
    pass


def test_get_posts_by_parameter_with_not_existing_value():
    pass
