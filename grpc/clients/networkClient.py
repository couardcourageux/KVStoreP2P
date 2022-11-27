import sys
import os

LOCAL_DIRECTORY = os.getcwd()
GRPC_DIR = os.path.join(LOCAL_DIRECTORY, "grpc")

sys.path.append(os.path.join(GRPC_DIR, "pyProtos"))
sys.path.append(os.path.join(LOCAL_DIRECTORY, "networking"))


import grpc
from typing import Tuple, Dict
import json

import ring_pb2_grpc
import ring_pb2


class NetworkClient:
    
    @classmethod
    def callForInit(self, distantAgentHost:str) -> None:
        with grpc.insecure_channel(distantAgentHost) as ch:
            stub = ring_pb2_grpc.NetworkCronJobStub(ch)
            req = ring_pb2.voidMsg()
            stub.callInitAgent(req)
            