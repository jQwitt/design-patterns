from src.object.SingletonObject import SingletonObject

class Application:
    obj: SingletonObject

    def run(self):
        print('Initializing...')

        try: 
            self.obj = SingletonObject()
        except TypeError:
            print('ERROR: to create this object you must use getInstance()')
        
        '''
            note: calling this again creates a new instance, although this shouldn't be possible
                this example mainly demonstrates the call pattern
        '''
        self.obj = SingletonObject.getInstance()    
        self.obj.doWork()

        print('Done!')

Application().run()