from Contracts.Model import Model


class Comment(Model):

    def get(self):
        self.data.json()
