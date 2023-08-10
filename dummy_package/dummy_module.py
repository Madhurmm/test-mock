import requests
from requests import Session


class DummyClass:
    session = None

    def __init__(self):
        self.session = Session()

    def get_request(self, url):
        response = self.session.get(url)
        print(response)
        return response.json()


if __name__ == '__main__':
    dum_req = DummyClass()
    dum_req.get_request('https://jsonplaceholder.typicode.com/todos/2')