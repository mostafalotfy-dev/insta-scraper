from Contracts.Model import Model


class Reel(Model):

    def get(self) -> dict:
        return self.data
