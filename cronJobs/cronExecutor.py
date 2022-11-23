from multiprocessing import Process

class CronJobber:
    
    def __init__(self, grpcPort:str):
        self.process = None
        self.port = grpcPort
       
    def run(self, port:str):
        pass

    def launch(self):
        self.process = Process(target=self.run, args=(self.port,))
        self.process.start()
        
    def stop(self):
        try:
            self.process.terminate()
        except :
            pass