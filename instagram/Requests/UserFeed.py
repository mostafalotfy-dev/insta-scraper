import json
import os

import requests

from Shared.Request import Request
from Shared.Utils.JsonReader import get_by_name


# fetch every thing using the instagram.json file
class UserFeed(Request):

    def __init__(self, name: str):
        super().__init__()

        record = self.get_record("user_feed_by_name")

        self.response = requests.get(record["url"]["raw"].format(name),
                                     headers=self.collect_headers(record["header"]))
        print(self.response.text)

    def get(self) -> dict:
        return self.response.json()
