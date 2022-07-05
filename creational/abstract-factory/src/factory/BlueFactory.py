from interfaces.factory import Factory
from src.object.BlueObject import BlueObject

class BlueFactory(Factory):
    def createObject(self):
        return BlueObject()