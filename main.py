import csv

import time

from dotenv import load_dotenv

from Requests.Search import Search

from argparse import ArgumentParser
from Requests.Like import Like

parser: ArgumentParser = ArgumentParser("insta_scraper")
parser.add_argument("name", help="type name to search Profile")

args = parser.parse_args()
load_dotenv()  # take environment variables from .env.
start = time.time()
search_results = Search(args.name).api()
csv_writer = csv.writer(open("users.csv", "w+", encoding="utf-8"))
csv_writer.writerow(["username", "link"])
for search_result in search_results:

    for user in search_results["users"]:
        csv_writer.writerow([user["user"]["username"], f"https://www.instagram.com/{user['user']['username']}"])

print(time.time() - start)
