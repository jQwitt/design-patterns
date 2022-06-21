from interfaces.factory import Factory
from src.object.RedObject import RedObject

class RedFactory(Factory):
    def createObject(self):
        return RedObject()
