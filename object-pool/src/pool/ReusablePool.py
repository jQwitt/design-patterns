from interfaces.object import Object
from src.object.Object import NetworkObject

AVAILABLE="0"
BUSY="1"

class ReusablePool:
    _objects = { AVAILABLE: [], BUSY: [] }
    _max_pool_size = -1

    def __createObject(self) -> bool:
        """ Create an Object and add it to the pool """
        if len(self._objects[BUSY]) + len(self._objects[AVAILABLE]) + 1 > self._max_pool_size:
            print("ERROR: max pool size reached, cannot instantiate new object")
            return False
        self._objects[AVAILABLE].append(NetworkObject())
        return True

    def acquireObject(self) -> Object | None:
        """ Acquire an Object from the pool """
        if len(self._objects[AVAILABLE]) == 0:
            if not self.__createObject():
                return None
            
        existingObject = self._objects[AVAILABLE].pop(0)
        self._objects[BUSY].append(existingObject)
        return existingObject

    def releaseObject(self, o: Object) -> bool:
        """ Release an Object from the pool """
        if o in self._objects[BUSY]:
            self._objects[BUSY].remove(o)
            self._objects[AVAILABLE].append(o)
            return True

        print("ERROR: attemtped to release available or non-existant object")
        return False

    '''
        Singleton Boilerplate code
        src: https://stackoverflow.com/questions/8212053/private-constructor-in-python
    '''
    __create_key = object()

    @classmethod
    def getInstance(cls, value: int):
        return ReusablePool(cls.__create_key, value)

    def __init__(self, create_key, value):
        assert(create_key == ReusablePool.__create_key), \
            "ReusablePool must be retrieved using ReusablePool.getInstance()"
        self._max_pool_size = value
    