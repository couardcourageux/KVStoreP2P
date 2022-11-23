import sys
import os

LOCAL_DIRECTORY = os.getcwd()
GRPC_DIR = os.path.join(LOCAL_DIRECTORY, "grpc")


sys.path.append(os.path.join(LOCAL_DIRECTORY, "networking"))
sys.path.append(os.path.join(GRPC_DIR, "pyProtos"))

import ring_pb2
import ring_pb2_grpc


class ClusterCronServicer(ring_pb2_grpc.ClusterCronJobServicer):
    def callPing(self, request, context):
        print("i need to ping")
        resp = ring_pb2.voidMsg()
        return resp
    
    def callCheckPings(self, request, context):
        print("i need check who pinged me")
        resp = ring_pb2.voidMsg()
        return resp