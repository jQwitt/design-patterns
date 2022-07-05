from src.adapter import Adapter
from src.service import Service

class Application:
    legacyService = Service()

    def run(self):
        print('Initializing...')

        adapter = Adapter(self.legacyService)

        print('Done!')

        adapter.taskA()
        adapter.taskB()

Application().run()