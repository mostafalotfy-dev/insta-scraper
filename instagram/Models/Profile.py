from Contracts.Model import Model


class Profile(Model):
    def get(self) -> dict:
        return self.data.json()
