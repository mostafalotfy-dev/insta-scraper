import requests

from Shared.Request import Request


class LogInfo(Request):
    def __init__(self):
        super().__init__()
        record = self.get_record("logging_info")
        requests.post(record["url"]["raw"], headers=self.collect_headers(record["header"]),
                      data=self.collect_post_data(record["body"]))
