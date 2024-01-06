import json
import os
from urllib.parse import urlparse

import requests
from requests import Response

from Shared.Utils.JsonReader import read_json, get_by_name


class Request:
    response: Response | dict
    host_name: str
    cookies: str
    headers: dict
    body: str | dict
    directory: str = "instagram"

    def __init__(self):

        opening = open(os.getcwd() + f"/{self.directory}/Requests/instagram.json", "r", encoding="utf-8")
        self.loaded_json = json.load(opening)

    def json(self) -> []:
        return self.response.json()

    def collect_headers(self, headers: dict):
        new_headers: dict = dict()
        cookies = read_json(f"{self.directory}/Requests/instagram.json")

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

    def collect_post_data(self, name: str) -> {}:
        post_data = {}
        record = get_by_name(self.loaded_json["item"], name)

        for item in record["body"]["urlencoded"]:
            post_data[item["key"]] = item['value']

        return post_data

    def get_record(self, name: str):
        insta = read_json(f"{self.directory}/Requests/instagram.json")["item"]

        for request in insta:
            if request["name"].find(name) != -1:
                return request["request"]
