import requests

from Request import Request
from Utils.JsonReader import read_json


class Info(Request):
    def __init__(self, media_id: str):
        super().__init__()
        headers = read_json("instagram.json")["item"][0]["request"]["header"]

        self.response = requests.get(
            f"https://instagram.com/api/v1/media/{media_id}/comments/?can_support_threading=true&permalink_enabled=false ",
            headers=self.collect_headers(headers))

    def get(self):
        return self.response.json()
