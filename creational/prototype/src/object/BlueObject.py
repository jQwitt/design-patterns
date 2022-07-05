import copy
from interfaces.object import Object

class BlueObject(Object):
    color: str = "blue"

    def clone(self):
        return copy.copy(self)
