import json
import os

import requests

from Request import Request
from Utils.JsonReader import get_by_name


# fetch every thing using the instagram.json file
class UserFeed(Request):

    def __init__(self, url_name: str, media_id: str):
        super().__init__()

        for i in self.loaded_json["item"]:

            if i["request"]["method"] == "get".upper():
                insta = get_by_name(i, url_name)

                if insta:
                    self.response = requests.get(insta["url"]["raw"].format(media_id),
                                                 headers=self.collect_headers(insta["header"]))
                    print(self.response.url)

    def api(self) -> dict:
        return self.response.json()
