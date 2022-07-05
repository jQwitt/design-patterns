from interfaces.object import Object

class Builder:
    def __init__(self) -> None:
        """ Init a new Object """
        pass

    def build(self) -> Object:
        """ Return the current Object """
        pass

    def addA(self, s: str) -> any:
        """ add an Object's A property """
        pass

    def addB(self, s: str) -> any:
        """ add an Object's B property """
        pass

    def addC(self, s: str) -> any:
        """ add an Object's C property """
        pass