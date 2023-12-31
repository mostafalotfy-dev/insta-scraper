import json

import requests

from Models.Clips import Clips
from Models.Feed import Feed
from Models.Like import Like
from Models.Profile import Profile
from Models.ProfileInfo import ProfileInfo
from Models.Reel import Reel
from Models.User import User
from Request import Request


# fetch every thing using the instagram.json file
class Batch(Request):

    def __init__(self, name: str):
        super().__init__()
        opening = open("instagram.json", "r", encoding="utf-8")
        j = json.load(opening)
        for i in j["item"]:
            if i["request"]["method"] == "post".upper():

                try:
                    data = requests.post(i["request"]["url"]["raw"].replace("islamfawzy_", name),
                                         headers=self.collect_headers(i["request"]["header"]))

                    print(f"post request {data.url} {data.status_code}")
                except:
                    print("post request timed out")
            elif i["request"]["method"] == "get".upper():

                url: str = i["request"]["url"]["raw"].replace("islamfawzy_", name)

                data = requests.get(url, headers=self.collect_headers(i["request"]["header"]))
                print(url, data.status_code)

                if i["name"].find("likes") != -1:
                    self.response["likes"] = Like(name="likes", data=data)
                if i["name"].find("clips") != -1:
                    self.response["clips"] = Clips(name="clips",
                                                   data=data)
                if i["name"].find("users") != -1:
                    self.response["users"] = User(name="users", data=data)
                if i["name"].find("profile_info") != -1:
                    self.response["profile_info"] = ProfileInfo(name="profile_info", data=data)
                if i["name"].find("reels") != -1:
                    self.response["reels"] = Reel(name="reels", data=data)
                if i["name"].find("profile") != -1:
                    self.response["profile"] = Profile(name="profile", data=data)
                if i["name"].find("feed") != -1:
                    self.response["feed"] = Feed(name="feed", data=data)

    def api(self):
        return self.response
