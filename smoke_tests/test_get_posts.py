import requests
from jsonschema import validate

response_schema = {
    'type' : 'object',
    'properties' : {
        'userId': {'type': 'number'},
        'id': {'type': 'number'},
        'title': {'type': 'string'},
        'body': {'type': 'string'},
    }
}


def test_get_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200
    validate(instance=response.json()[0], schema=response_schema)
