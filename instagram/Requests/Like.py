
from time import sleep

import requests

from Shared.Request import Request
from instagram.Requests.LogInfo import LogInfo


class Like(Request):
    def __init__(self, feeds: []):
        super().__init__()
        record = self.get_record("likes")
        headers = self.collect_headers(record["header"])
        self.likes = []

        for feed in feeds:
            response = requests.get(
                record["url"]["raw"].format(feed["pk"]),
                headers=headers)

            self.likes.append(response.json())
            LogInfo()
            sleep(1)



    def get(self):
        return self.likes
