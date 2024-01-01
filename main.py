import csv

import time

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

    search_results = Search(f"#{args.name}").api()
else:
    search_results = Search(args.name).api()
csv_writer = csv.writer(open("search_results.csv", "w+", encoding="utf-8"))
csv_writer.writerow(["username", "link"])

for search_result in search_results:
    for user in search_results["users"]:
        user_feeds = UserFeed(user["user"]["username"]).get()["items"]

        comments_data = Comment(user_feeds).get()
        print(comments_data)
        for comments in comments_data:
            for comment in comments["comments"]:
                csv_writer.writerow([comment["user"]["username"], f"https://www.instagram.com/{comment['user']['username']}"])


print(time.time() - start)
