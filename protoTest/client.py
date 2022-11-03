import grpc
import ring_pb2
import ring_pb2_grpc

import time

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = ring_pb2_grpc.Node2NodeStub(channel)
        req = ring_pb2.IDReqMsg()
        req.token = "yolo"
        resp = stub.obtainId(req)
        print(resp)
        
        
if __name__ == '__main__':
    run()