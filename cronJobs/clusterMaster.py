import sys
import os

LOCAL_DIRECTORY = os.getcwd()
GRPC_DIR = os.path.join(LOCAL_DIRECTORY, "grpc")


sys.path.append(os.path.join(GRPC_DIR, "clients"))



from threading import Thread
import time
import asyncio
from cronExecutor import CronJobber

from clusterCronClient import ClusterCronClient



class ClusterMaster(CronJobber):
    
    def __init__(self, port:str):
        super().__init__(port)
        
        
    
    
    #override
    def run(self, port:str):
        async def main():
            while True:
                await self.checkForPings(port)
                await self.pingOtherNodes(port)
                
        print("yeh")
        loop = asyncio.get_event_loop()
        loop.create_task(main())
        loop.run_forever()
        # asyncio.run(main())
        
    async def checkForPings(self, port:str):
        ClusterCronClient.callCheckPingMethod(port)
        await asyncio.sleep(3)
        
    async def pingOtherNodes(self, port:str):
        ClusterCronClient.callPingAgentMethod(port)
        await asyncio.sleep(3)
        
        
if __name__ == '__main__':
    master = ClusterMaster("5000")
    master.launch()
    # master.run(master.port)
    time.sleep(15)
    master.stop()
    print("fun")
        


    