from interfaces.object import Object
from src.object.BlueObject import BlueObject

class Application:

    def run(self):
        print('Initializing...')
        
        blue = BlueObject()
        blue.color = "dark blue"
        blueClone = blue.clone()

        print('Done!')

        print(blue)
        print(blue.color)
        print(blueClone)
        print(blueClone.color)

Application().run()