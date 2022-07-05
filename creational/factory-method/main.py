from interfaces.creator import Creator
from interfaces.object import Object
from src.creator.RedCreator import RedCreator
from src.creator.BlueCreator import BlueCreator

class Application:
    creator: Creator

    def __init__(self, creator: Creator):
        self.creator = creator

    def run(self):
        print("Initializing...")

        obj: Object = self.creator.createObject()

        print('creating object with property: {}'.format(obj.property))

app = Application(BlueCreator())
app.run()