import sys
import os

LOCAL_DIRECTORY = os.getcwd()
GRPC_DIR = os.path.join(LOCAL_DIRECTORY, "grpc")


sys.path.append(os.path.join(GRPC_DIR, "clients"))


import time

from cronExecutor import CronJobber
import json

from networkClient import NetworkClient

class InitExecutor(CronJobber):
    def __init__(self, grpcPort: str):
        super().__init__(grpcPort)
        
        
    def run(self, port:str):
        time.sleep(5)
        NetworkClient.callForInit("localhost:" + port)
        
        