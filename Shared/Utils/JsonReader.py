import json
import os


def read_json(file_name: str) -> dict:
    return json.load(open(os.getcwd() + "/" + file_name, "r", encoding="utf-8"))


def write_json(output: str, data):
    with open(output, "w") as f:
        f.write(data)


def filter_by_name(data: [], name: str):
    for record in data:
        if record.find(name) != -1:
            return data[record]


def get_by_name(data, name: str):
    for l in data:
        if l["name"] == name:

            return l["request"]


