import requests

from Shared.Request import Request


class Follower(Request):
    def __init__(self, user_id: int):
        super().__init__()
        record = self.get_record("followers")
        self.response = requests.get(record["url"]["raw"].format(user_id),
                                     headers=self.collect_headers(record["header"]))


    def get(self):
        return self.response.json()
