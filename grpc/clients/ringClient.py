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





class RingClient:
    
    def __init__():
        pass

    @classmethod
    def join_network(self, distantAgentHost: str) -> Tuple[str, str]:
        with grpc.insecure_channel(distantAgentHost) as ch:
            stub = ring_pb2_grpc.Node2NodeStub(ch)
            req = ring_pb2.IDReqMsg()
            req.token = "yolo"
            resp = stub.obtainId(req)
        
        return resp.agentId, resp.nodeId
    
    @classmethod
    def searchAddr(self, distantAgentHost: str, NodeId:str) -> Dict:
        with grpc.insecure_channel(distantAgentHost) as ch:
            stub = ring_pb2_grpc.Node2NodeStub(ch)
            req = ring_pb2.IdRingMsg()
            req.ringId = NodeId
            resp = stub.findAddr(req)
            
        
        return json.loads(resp.NodeDict)
    
    