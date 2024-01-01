from time import sleep

import requests

from Shared.Request import Request
from instagram.Requests.LogInfo import LogInfo


class Comment(Request):
    def __init__(self, private_key: str):
        super().__init__()
        record = self.get_record("comments")
        headers = self.collect_headers(record["header"])

        self.response = requests.get(
            record["url"]["raw"].format(private_key),
            headers=headers)

        sleep(1)

    def get(self):
        return self.response.json()
