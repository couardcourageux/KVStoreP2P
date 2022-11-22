import sys
import os

LOCAL_DIRECTORY = os.getcwd()
GRPC_DIR = os.path.join(LOCAL_DIRECTORY, "grpc")


sys.path.append(os.path.join(LOCAL_DIRECTORY, "networking"))
sys.path.append(os.path.join(GRPC_DIR, "pyProtos"))

import ring_pb2
import ring_pb2_grpc


from utilitary import create_agent_id, create_node_id
from localAgent import LocalAgent
from agent_and_dnode import Agent


class ClusterServicer(ring_pb2_grpc.AgentClusterServicer):
    def joinReq(self, request, context):
        # ag = LocalAgent.getAgent()
        print("joinReq requested")
        print(request)
        dNode = LocalAgent.getAgent().hosting
        joiningAgent = Agent(   request.agentLoc.agentId, 
                                request.agentLoc.ip, 
                                request.agentLoc.port, 
                                request.agentType, 
                                request.capacity, dNode
                            )
        dNode.agents[joiningAgent.agent_id] = joiningAgent
        
        resp = ring_pb2.ResponseMsg()
        resp.errorCode = 0
        resp.respStatus = False
        return resp