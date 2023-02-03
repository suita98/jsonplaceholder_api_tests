import requests


class ApiClient:

    def __init__(self):
        self.host = 'https://jsonplaceholder.typicode.com'

    def get_posts(self, params={}):
        response = requests.get(f'{self.host}/posts', params=params)
        return response
