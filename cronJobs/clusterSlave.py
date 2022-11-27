import sys
import os

LOCAL_DIRECTORY = os.getcwd()
GRPC_DIR = os.path.join(LOCAL_DIRECTORY, "grpc")


sys.path.append(os.path.join(GRPC_DIR, "clients"))

import asyncio

from cronExecutor import CronJobber
from clusterCronClient import ClusterCronClient


class ClusterSlave(CronJobber):
    
    def __init__(self, port:str):
        super().__init__(port)
    
    #override
    def run(self, port:str):
        async def main():
            while True:
                await self.pingMaster(port)
                
        asyncio.run(main())
    
    async def pingMaster(self, port:str):
        ClusterCronClient.callPingAgentMethod(port)
        await asyncio.sleep(3)

   