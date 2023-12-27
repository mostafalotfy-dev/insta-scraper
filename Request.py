from random import random


class Request:
    res: dict | str
    host_name: str
    cookies: str
    headers: dict
    body: str | dict

    def __init__(self):
        csrftoken= random()
        self.host_name = "https://www.instagram.com/"
        self.cookies = ""
        self.headers = {"User-Agent": f'{random()}',
                        "X-Csrftoken": f"{csrftoken}",
                        "X-Ig-App-Id": "936619743392459",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Sec-Fetch-Site": "same-origin",
                        "Host": self.host_name.replace("https://", "").replace(".com/", ".com"),
                        "Cookie": self.cookies,
                        }
        self.body = ""
        self.res = dict()

    def json(self) -> dict:
        return self.res
