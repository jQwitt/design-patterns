from interfaces.creator import Creator
from interfaces.object import Object
from src.object.RedObject import RedObject

class RedCreator(Creator):
    def createObject(self) -> Object:
        """ Create a Red Object """
        return RedObject()
