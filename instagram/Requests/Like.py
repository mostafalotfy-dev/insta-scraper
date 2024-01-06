from time import sleep

import requests

from Shared.Request import Request
from instagram.Requests.LogInfo import LogInfo


class Like(Request):
    def __init__(self, user: dict):
        super().__init__()
        record = self.get_record("likers")
        headers = self.collect_headers(record["header"])

        self.response = requests.get(
            record["url"]["raw"].format(user["pk"]),
            headers=headers)



    def get(self):
        return self.response.json()
