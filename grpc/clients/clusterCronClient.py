import sys
import os

LOCAL_DIRECTORY = os.getcwd()
GRPC_DIR = os.path.join(LOCAL_DIRECTORY, "grpc")


# sys.path.append(os.path.join(LOCAL_DIRECTORY, "networking"))
sys.path.append(os.path.join(GRPC_DIR, "pyProtos"))


import grpc
import ring_pb2
import ring_pb2_grpc


class ClusterCronClient:
    def __init__(self) -> None:
        pass
    
    @classmethod
    def callPingAgentMethod(self, port:str) -> None:
        with grpc.insecure_channel("localhost:" + port) as ch:
            stub = ring_pb2_grpc.ClusterCronJobStub(ch)
            req = ring_pb2.voidMsg()
            stub.callPing(req)
            
    @classmethod
    def callCheckPingMethod(self, port:str) -> None:
        with grpc.insecure_channel("localhost:" + port) as ch:
            stub = ring_pb2_grpc.ClusterCronJobStub(ch)
            req = ring_pb2.voidMsg()
            stub.callCheckPings(req)
        