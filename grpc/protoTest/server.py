from concurrent import futures
import time


import grpc
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
    
    
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    ring_pb2_grpc.add_Node2NodeServicer_to_server(RingServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()
    
if __name__ == '__main__':
    serve()