import secrets
import mmh3


import grpc
from concurrent import futures
from multiprocessing import Process


import ring_pb2_grpc
import ring_pb2

#########################################
def create_secret_string(n: int) -> str:
    return secrets.token_hex(n)

def create_agent_id() -> str:
    return create_secret_string(256)


def create_node_id() -> str:
    return create_secret_string(128)
#########################################

def join_network(distantAgentHost: str):
    with grpc.insecure_channel(distantAgentHost) as ch:
        stub = ring_pb2_grpc.Node2NodeStub(ch)
        req = ring_pb2.IDReqMsg()
        req.token = "yolo"
        resp = stub.obtainId(req)
    
    return resp.agentId, resp.nodeId

