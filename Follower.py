import requests

from Request import Request


class Follower(Request):
    def __init__(self, followId: int):
        super().__init__()
        self.prefix = f"api/v1/friendships/{followId}/followers/?hl=en"

        self.res = requests.get(self.host_name + self.prefix, headers=self.headers).json()

    def get(self):
        for follower in self.res["users"]:
            yield follower
