from Contracts.Model import Model


class ProfileInfo(Model):
    def get(self):
        return self.data.json()["data"]["user"]
