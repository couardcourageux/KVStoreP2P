import sys
import os

LOCAL_DIRECTORY = os.getcwd()
GRPC_DIR = os.path.join(LOCAL_DIRECTORY, "grpc")


sys.path.append(os.path.join(GRPC_DIR, "clients"))




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
            asyncio.sleep(3)
            while True:
                try:
                    await self.checkForPings(port)
                    await self.pingOtherNodes(port)
                except:
                    asyncio.sleep(1)
                
        asyncio.run(main())
        # asyncio.run(main())
        
    async def checkForPings(self, port:str):
        ClusterCronClient.callCheckPingMethod(port)
        await asyncio.sleep(3)
        
    async def pingOtherNodes(self, port:str):
        return
        await asyncio.sleep(3)
        
        

        


    