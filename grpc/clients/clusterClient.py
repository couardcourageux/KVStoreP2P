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
from agent_and_dnode import Agent

class ClusterClient:
    def __init__():
        pass
    
    @classmethod
    def joinNode(self, distantAgentHost:str, agent: Agent) -> None:
        with grpc.insecure_channel(distantAgentHost) as ch:
            stub = ring_pb2_grpc.AgentClusterStub(ch)
            req = ring_pb2.AgentDescMsg()
            req.agentDict = json.dumps(agent.toDict())
            resp = stub.joinReq(req)
            
        if resp.accepted:    
            return json.loads(resp.NodeDict)
        return None
    
    @classmethod
    def sendUpdateNodeData(self, distantAgentHost:str, nodeDict:str) -> None:
        with grpc.insecure_channel(distantAgentHost) as ch:
            stub = ring_pb2_grpc.AgentClusterStub(ch)
            req = ring_pb2.NodeDescMsg()
            req.NodeDict = nodeDict
            stub.udpdateNode(req)
        return None
            