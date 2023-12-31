import pandas
from dotenv import load_dotenv
from Batch import Batch
from argparse import ArgumentParser
from Info import Info
from Utils.JsonReader import filter_by_name

parser: ArgumentParser = ArgumentParser("insta_scraper")
parser.add_argument("name", help="type name to search Profile")
args = parser.parse_args()
load_dotenv()  # take environment variables from .env.
data = Batch(args.name).api()

for user in filter_by_name(data, "clips").get()["items"]:
    data = Info(user["pk"]).get()

    pandas.DataFrame(data["comments"]).to_csv(open("users.csv", "a+", encoding="utf-8"),index=False)


