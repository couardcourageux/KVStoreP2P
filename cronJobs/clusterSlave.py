from threading import Thread


from cronExecutor import CronJobber



class ClusterSlave(CronJobber):
    
    def __init__(self):
        super().__init__()
    
    #override
    def run(self, port:str):
        pass

   