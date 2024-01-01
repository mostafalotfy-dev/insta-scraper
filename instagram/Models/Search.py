from requests import Response

from Contracts.Model import Model


class Search(Model):

    def get(self) -> dict:
        return self.data.json()["data"]["xdt_api__v1__fbsearch__topsearch_connection"]

    def users(self):
        return self.get()["users"]

    def hashtags(self):
        return self.get()["hashtags"]
