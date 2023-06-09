from abc import ABC, abstractmethod
import requests


class BaseClient(ABC):
    @abstractmethod
    def make_get_request(self):
        pass

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass


class ConcreteBaseClient():
    def __init__(self, base_url):
        self.base_url = base_url

    def make_get_request(self):
        res = requests.get(self.base_url)
        return res.json()

    def __call__(self, *args, **kwargs):
        return self.make_get_request()


class WikiClient(ConcreteBaseClient):
    pass


class PlosClient(ConcreteBaseClient):
    pass


class Worker:
    def __init__(self, wiki_client: WikiClient, plos_client: PlosClient):
        self.wiki_client = wiki_client
        self.plos_client = plos_client

    def __call__(self, *args, **kwargs):
        return {'wiki_data': self.wiki_client(),
                'plos_data': self.plos_client()}
