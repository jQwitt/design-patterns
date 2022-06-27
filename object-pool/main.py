from interfaces.object import Object
from src.pool.ReusablePool import ReusablePool

class Application:
    workers: ReusablePool

    def run(self):
        print('Initializing...')
        self.workers = ReusablePool.getInstance(2)
        print('Done!')

        worker1 = self.workers.acquireObject()
        worker1.doWork()
        worker2 = self.workers.acquireObject()
        worker2.doWork()
        worker3 = self.workers.acquireObject()

        self.workers.releaseObject(worker1)

        worker3 = self.workers.acquireObject()
        worker3.doWork()

Application().run()