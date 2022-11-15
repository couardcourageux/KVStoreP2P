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

class RingServicer(ring_pb2_grpc.Node2NodeServicer):
    def obtainId(self, request, context):
        print(request)
        # print(LocalAgent.getAgent().hosting.dNode_id)
        rep = ring_pb2.IDReqRespMsg()
        rep.errorCode = 0
        rep.agentId = create_agent_id()
        # rep.nodeId = create_node_id()
        rep.nodeId = LocalAgent.getAgent().hosting.dNode_id
        
        return rep