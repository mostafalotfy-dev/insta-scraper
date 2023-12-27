import requests

from Request import Request


class Like(Request):
    def __init__(self, mediaId: int):
        super().__init__()
        self.prefix = f"api/v1/media/{mediaId}/likers/"
        self.res = requests.get(self.host_name + self.prefix, headers=self.headers).json()

    def get(self):
        for like in self.res["users"]:
            yield like
