from interfaces.builder import Builder
from interfaces.object import Object

class ObjectBuilder(Builder):
    obj: Object

    def __init__(self):
        self.obj = Object()

    def build(self):
        return self.obj

    def addA(self, s):
        self.obj.propertyA = s
        return self

    def addB(self, s):
        self.obj.propertyB = s
        return self

    def addC(self, s):
        self.obj.propertyC = s
        return self