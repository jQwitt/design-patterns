import random

class SingletonObject:
    task: str = ""

    def doWork(self):
        print("doing work for task: {}".format(self.task))

    '''
        Singleton Boilerplate code
        src: https://stackoverflow.com/questions/8212053/private-constructor-in-python
    '''
    __create_key = object()

    @classmethod
    def getInstance(cls):
        return SingletonObject(cls.__create_key)

    def __init__(cls, create_key):
        assert(create_key == SingletonObject.__create_key), \
            "SingletonObject must be retrieved using SingletonObject.getInstance()"
        if cls.task == "":
            cls.task = random.randint(100, 110)
