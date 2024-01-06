import json

import requests

from Shared.Request import Request
from Shared.Utils.JsonReader import get_by_name, read_json, filter_by_name


# fetch every thing using the instagram.json file
class Search(Request):

    def __init__(self, name: str):
        super().__init__()
        items = read_json(f"/{self.directory}/Requests/instagram.json")
        insta_file = get_by_name(self.loaded_json["item"], "search")
        headers = self.collect_headers(insta_file["header"])
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        headers["Cookie"] = items["variable"][0]["value"]
        headers["X-Csrftoken"] = items["variable"][1]["value"]  # csrf variable
        post_data = self.collect_post_data("search")
        variables = json.loads(post_data["variables"])
        variables["data"]["query"] = name
        post_data["variables"] = json.dumps(variables)
        del variables

        self.response = requests.post(insta_file["url"]["raw"], headers=headers,
                                      data=post_data)
        print(self.response.text)

    def api(self) -> dict:
        return self.response.json()["data"]["xdt_api__v1__fbsearch__topsearch_connection"]
