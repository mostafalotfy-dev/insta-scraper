from random import random
from time import sleep
from typing import List

import requests
from requests import Response

from Contracts.Model import Model


class Clips(Model):

    def get(self) -> dict:
        return self.data.json()
