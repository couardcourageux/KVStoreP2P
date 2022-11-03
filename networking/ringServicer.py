import sys
import os

LOCAL_DIRECTORY = os.getcwd()
sys.path.append(os.path.join(LOCAL_DIRECTORY, "pyProtos"))



import ring_pb2
import ring_pb2_grpc

from networking_lib import create_agent_id, create_node_id

class RingServicer(ring_pb2_grpc.Node2NodeServicer):
    def obtainId(self, request, context):
        print(request)
        rep = ring_pb2.IDReqRespMsg()
        rep.errorCode = 0
        rep.agentId = create_agent_id()
        rep.nodeId = create_node_id()
        
        return rep