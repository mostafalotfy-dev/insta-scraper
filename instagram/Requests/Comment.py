
from time import sleep

import requests

from Shared.Request import Request
from instagram.Requests.LogInfo import LogInfo


class Comment(Request):
    def __init__(self, feeds: []):
        super().__init__()
        record = self.get_record("comments")
        headers = self.collect_headers(record["header"])
        self.comments = []

        for feed in feeds:
            response = requests.get(
                record["url"]["raw"].format(feed["pk"]),
                headers=headers)

            self.comments.append(response.json())
            LogInfo()
            sleep(1)



    def get(self):
        return self.comments
