from Contracts.Model import Model


class Feed(Model):
    def get(self) -> dict:
        return self.data.json()
