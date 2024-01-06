import csv
import time

import requests.exceptions
from dotenv import load_dotenv
from instagram.Requests.Comment import Comment
from instagram.Requests.Follower import Follower
from instagram.Requests.Like import Like
from instagram.Requests.Media import Media

from instagram.Requests.Search import Search

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
    count = 0
    followers_list = []

    for user in search_results["users"]:

        followers = Follower(user["user"]["pk"]).get()  # get comments
        if "spam" in followers:
            print("detected as spam")
            media = Media(user["user"]["pk"]).get()
            for item in media["items"]:
                likes = Like(item).get()
                print(likes)
                if "spam" in likes.keys():
                    comments = Comment(item["pk"]).get()
                    for comment in comments["comments"]:
                        csv_writer.writerow(
                            [comment["user"]["username"], f"https://www.instagram.com/{comment['user']['username']}"])
                elif likes["status"] == "fail":
                    continue
                else:
                    for like in likes["users"]:
                        csv_writer.writerow(
                            [like["username"], f"https://www.instagram.com/{like['username']}"])
        else:
            # iterate over each comment
            for follower in followers["users"]:
                count += 1
                print(count)

                print(time.time() - start)
                csv_writer.writerow(
                    [follower["username"], f"https://www.instagram.com/{follower['username']}"])


except requests.exceptions.ReadTimeout:
    print("connection went down")
except requests.exceptions.ConnectionError:
    print("connection error")
