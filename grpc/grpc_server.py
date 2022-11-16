import sys
import os

LOCAL_DIRECTORY = os.getcwd()
GRPC_DIR = os.path.join(LOCAL_DIRECTORY, "grpc")

sys.path.append(os.path.join(GRPC_DIR, "servicers"))
sys.path.append(os.path.join(GRPC_DIR, "pyProtos"))


from concurrent import futures
import grpc
from ringServicer import RingServicer

import ring_pb2_grpc




def get_server(host, max_workers=10):
    serv = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    ring_pb2_grpc.add_Node2NodeServicer_to_server(RingServicer(), serv)
    #...
    serv.add_insecure_port(host)
    return serv
