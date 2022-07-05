import random
from interfaces.object import Object

class NetworkObject(Object):
    def __init__(self):
        self._title = "Networking task - {}".format(random.randint(100, 150))

    def doWork(self):
        print("doing work: {}".format(self._title))
        