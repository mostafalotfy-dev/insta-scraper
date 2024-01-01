import csv
import time

import requests.exceptions
from dotenv import load_dotenv
from instagram.Requests.Comment import Comment
from instagram.Requests.Search import Search
from instagram.Requests.UserFeed import UserFeed
from argparse import ArgumentParser

parser: ArgumentParser = ArgumentParser("insta_scraper")
parser.add_argument("name", help="type name to search Profile")
parser.add_argument("-hashtag", default=False, type=bool, required=False)
args = parser.parse_args()
load_dotenv()  # take environment variables from .env.
start = time.time()
if args.hashtag:
    search_results = Search(f"#{args.name}").api()  # get search results for hashtag
else:
    search_results = Search(args.name).api()  # get search results by name
csv_writer = csv.writer(open("search_results.csv", "w+", encoding="utf-8"))  # create csv write
csv_writer.writerow(["username", "link"])
# iterate over each search result
try:
    for search_result in search_results:
        for user in search_results["users"]:
            user_feeds = UserFeed(user["user"]["username"]).get()["items"]  # get user posts
            for item in user_feeds:
                comments_data = Comment(item["pk"]).get()  # get comments
                # iterate over each comment
                for comment in comments_data["comments"]:
                    csv_writer.writerow(
                        [comment["user"]["username"], f"https://www.instagram.com/{comment['user']['username']}"])
except requests.exceptions.ReadTimeout:
    print("connection went down")
except requests.exceptions.ConnectionError:
    print("connection error")

print(time.time() - start)
