import sys
import os

LOCAL_DIRECTORY = os.getcwd()
GRPC_DIR = os.path.join(LOCAL_DIRECTORY, "grpc")


sys.path.append(os.path.join(LOCAL_DIRECTORY, "networking"))
sys.path.append(os.path.join(GRPC_DIR, "pyProtos"))

import ring_pb2
import ring_pb2_grpc

import json

# from utilitary import create_agent_id, create_node_id
from localAgent import LocalAgent
from agent_and_dnode import Agent, DNode
from clusterLogic import joiningClusterProc


class ClusterServicer(ring_pb2_grpc.AgentClusterServicer):
    def joinReq(self, request, context):        
        result = joiningClusterProc(request.agentDict)

        resp = ring_pb2.JoinClusterResp()
        resp.accepted = result["accepted"]
        resp.NodeDict = result["NodeDict"]
        return resp
    
    def udpdateNode(self, request, context):
        dict = json.loads(request.NodeDict)
        nodeId = DNode.importFromDict(dict)
        LocalAgent.getAgent().setHosting(DNode.get(nodeId))
        
        print(LocalAgent.getAgent().hosting().toDict())
        
        
        return ring_pb2.voidMsg()