import sys
import os

LOCAL_DIRECTORY = os.getcwd()
sys.path.append(os.path.join(LOCAL_DIRECTORY, "pyProtos"))



import ring_pb2
import ring_pb2_grpc

class RingServicer(ring_pb2_grpc.Node2NodeServicer):
    def obtainId(self, request, context):
        print(request)
        rep = ring_pb2.IDReqRespMsg()
        rep.errorCode = 0
        rep.agentId = "agentId"
        rep.nodeId = "NodeId"
        
        return rep