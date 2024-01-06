from time import sleep

import requests

from Shared.Request import Request
from instagram.Requests.LogInfo import LogInfo


class Comment(Request):
    def __init__(self, private_key: str):
        super().__init__()

        self.private_key = private_key

    def get(self):
        record = self.get_record("comments")
        headers = self.collect_headers(record["header"])

        self.response = requests.get(
            record["url"]["raw"].format(self.private_key),
            headers=headers)
        print(self.response.text)
        return self.response.json()
