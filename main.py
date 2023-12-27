import pandas as pd

from Clips import Clips

from Like import Like
from Profile import Profile

ids: [int] = []
usernames: [str] = []
for profile in Profile(name="ahmed").get():
    print(profile.data.user.id)
    for clip in Clips().get(profile.data.user.id):
        print(clip["media"]["pk"])
        for like in Like(clip["media"]["pk"]).get():
            usernames.append(like["username"])
df = pd.DataFrame(usernames)
df.to_csv("users.csv", mode="a+", index=False)
