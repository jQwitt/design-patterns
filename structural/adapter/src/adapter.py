from interfaces.client import Client
from src.service import Service

class Adapter(Client):
    service: Service

    def __init__(self, s: Service):
        self.service = s

    def taskA(self):
        self.service.serverWorkA()
        

    def taskB(self):
        self.service.serverWorkB()