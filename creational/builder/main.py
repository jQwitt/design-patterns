from interfaces.builder import Builder
from interfaces.object import Object

from src.builder import ObjectBuilder

class Application:
    builder: Builder
    obj: Object

    def run(self):
        print("Initializing...")

        self.builder = ObjectBuilder

        self.obj = self \
            .builder() \
            .addA("step 1") \
            .addB("step 2") \
            .addC("step 3") \
            .build()

        print('creating object with properties:\n{}\n{}\n{}'.format(self.obj.propertyA, self.obj.propertyB, self.obj.propertyC))

Application().run()