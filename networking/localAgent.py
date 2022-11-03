from dataclasses import dataclass, field
from typing import List, Dict

import grpc
from concurrent import futures
from threading import Thread
from multiprocessing import Process

from nClasses import Agent, DNode

from ringServicer import RingServicer
import ring_pb2_grpc



class LocalAgent:
    
    __agent = Agent("need_init", "0.0.0.0", "00")
    __grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    __grpcsServProc = None

    @classmethod
    def _serveGRPC(self):
        ring_pb2_grpc.add_Node2NodeServicer_to_server(RingServicer(), self.__grpcServer)
        self.__grpcServer.add_insecure_port("localhost:50051")
        self.__grpcServer.start()
        self.__grpcServer.wait_for_termination()
      
    @classmethod  
    def serveGRPC(self):
        # self.__grpcsServTh = Thread(target=self._serveGRPC,args=[])
        # self.__grpcsServTh.start()
        self.__grpcsServProc = Process(target=self._serveGRPC, args=())
        self.__grpcsServProc.start()
    
    @classmethod
    def closeServers(self):
            self.__grpcsServProc.terminate()
        
        
if __name__ == '__main__':
    LocalAgent.serveGRPC()
