from requests import Response

from Contracts.Model import Model


class User(Model):

    def get(self) -> dict:
        return self.data.json()