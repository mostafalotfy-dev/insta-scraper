from urllib.parse import urlparse

from requests import Response
from urllib3.util import Url

from Contracts.Model import Model
from Utils.JsonReader import read_json


class Request:
    response: {} = {}
    host_name: str
    cookies: str
    headers: dict
    body: str | dict

    def __init__(self):
        self.response = {}

    def json(self) -> []:
        return self.response

    def collect_headers(self, headers: dict):
        new_headers: dict = dict()
        cookies = read_json("instagram.json")

        for header in headers:
            if header["key"] == "cookie":
                new_headers["Cookie"] = cookies["variable"][0]["value"]
            else:
                new_headers[header["key"].title()] = header["value"]

        return new_headers

    def is_json(self, response: Response):
        try:
            response.json()
            return True
        except:
            return False

    def parse_url(self, url: str):
        url = urlparse(url)
        return url
