from interfaces.factory import Factory
from src.factory.RedFactory import RedFactory
from src.factory.BlueFactory import BlueFactory

env = "red"

class Application:
    factory: Factory

    def run():
        print("Initializing...")

        if env == "red":
            factory = RedFactory()
        elif env == "blue":
            factory = BlueFactory()
        else:
            exit(1)

        print('creating object with property: {}'.format(factory.createObject().property))

Application.run()