import requests

from Request import Request


class Follower(Request):

    def get(self):
        return self.response.json()

