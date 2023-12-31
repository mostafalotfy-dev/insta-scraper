from Contracts.Model import Model


class Like(Model):

    def get(self) -> dict:
        return self.data.json()
