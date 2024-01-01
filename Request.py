import json
import os
from urllib.parse import urlparse

import requests
from requests import Response

from Utils.JsonReader import read_json, get_by_name


class Request:
    response: Response
    host_name: str
    cookies: str
    headers: dict
    body: str | dict

    def __init__(self):
        opening = open(os.getcwd() + "/Requests/instagram.json", "r", encoding="utf-8")
        self.loaded_json = json.load(opening)
        sso = get_by_name(data=self.loaded_json["item"],name="ig_sso")
        requests.post(sso["url"]["raw"],headers=self.collect_headers(sso["header"]))

    def json(self) -> []:
        return self.response

    def collect_headers(self, headers: dict):
        new_headers: dict = dict()
        cookies = read_json("Requests/instagram.json")

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

    def collect_post_data(self, loaded_json) -> {}:
        post_data = {}
        for data in loaded_json["urlencoded"]:
            post_data[data["key"]] = data['value']

        return post_data
