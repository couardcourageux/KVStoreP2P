import sys
import os

LOCAL_DIRECTORY = os.getcwd()
GRPC_DIR = os.path.join(LOCAL_DIRECTORY, "grpc")

sys.path.append(os.path.join(GRPC_DIR, "pyProtos"))
sys.path.append(os.path.join(LOCAL_DIRECTORY, "networking"))


import grpc
from typing import Tuple, Dict


import ring_pb2_grpc
import ring_pb2
from agent_and_dnode import Agent

class ClusterClient:
    def __init__():
        pass
    
    @classmethod
    def joinNode(self, distantAgentHost:str, agent: Agent) :
        with grpc.insecure_channel(distantAgentHost) as ch:
            stub = ring_pb2_grpc.AgentClusterStub(ch)
            sub = ring_pb2.IpPortMsg()
            sub.agentId = agent.agent_id
            sub.ip = agent.ip
            sub.port = agent.port
            
            req = ring_pb2.AgentDescMsg()
            req.agentLoc.CopyFrom(sub)
            req.agentType = agent.agent_type
            req.capacity = agent.capacity
            resp = stub.joinReq(req)
            
        print(resp)