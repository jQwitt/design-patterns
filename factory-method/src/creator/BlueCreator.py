from interfaces.creator import Creator
from interfaces.object import Object
from src.object.BlueObject import BlueObject

class BlueCreator(Creator):
    def createObject(self) -> Object:
        """ Create a Blue Object """
        return BlueObject()
