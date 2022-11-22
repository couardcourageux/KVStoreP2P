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
# from agent_and_dnode import Agent, DNode

class RingServicer(ring_pb2_grpc.Node2NodeServicer):
    def obtainId(self, request, context) -> ring_pb2.IDReqRespMsg:
        rep = ring_pb2.IDReqRespMsg()
        rep.errorCode = 0
        rep.agentId = create_agent_id()
        rep.nodeId = LocalAgent.getAgent().hosting().dNode_id
        return rep
    
    
    
    def findAddr(self, request, context) -> ring_pb2.NodeAddrMsg:
        rep = ring_pb2.NodeAddrMsg()
        print(request)
        # pour le moment
        ag = LocalAgent.getAgent()
        add1 = ring_pb2.IpPortMsg()
        add2 = ring_pb2.IpPortMsg()
        add1.agentId = ag.agent_id
        add1.ip = ag.ip
        add1.port = ag.port
        
        add2.agentId = ""
        add2.ip = ""
        add2.port = ""
        
        rep.errorCode = 0
        rep.NodeId = ag.hosting().dNode_id
        rep.master.CopyFrom(add1)
        rep.backup.CopyFrom(add2)
        return rep
    
    
        