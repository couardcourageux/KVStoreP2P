from dataclasses import dataclass, field
from typing import List, Dict

import grpc
from concurrent import futures
from multiprocessing import Process

from nClasses import Agent, DNode

from ringServicer import RingServicer
import ring_pb2_grpc
import ring_pb2
from networking_lib import create_agent_id, create_node_id, join_network


class LocalAgent:
    
    __agent = Agent("need_init", "localhost", "00")
    __grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    __grpcsServProc = None
    
    @classmethod
    def _setAgent(self, id:str, port:str):
        self.__agent.agent_id = id
        self.__agent.ip = "localhost"
        self.__agent.port = port
        
    @classmethod
    def initAgent(self, port: str):
        self._setAgent(create_agent_id(), port)

        
    @classmethod
    def initNetwork(self, port: str):
        self._setAgent(create_agent_id(), port)
        dNode = DNode(create_node_id(), None, [self.__agent])
        self.__agent.hosting[dNode.dNode_id] = dNode
        
    @classmethod
    def showMe(self):
        print(self.__agent.hosting)
        
        
        
    @classmethod
    def joinNetwork(self, distantAgentHost: str):
        agent_id, node_id = join_network(distantAgentHost)
        print(f"joining network: agent_id: {agent_id[:20]}")
        self.__agent.agent_id = agent_id



    @classmethod
    def _serveGRPC(self, host):
        ring_pb2_grpc.add_Node2NodeServicer_to_server(RingServicer(), self.__grpcServer)
        self.__grpcServer.add_insecure_port(host)
        self.__grpcServer.start()
        self.__grpcServer.wait_for_termination()
      
    @classmethod  
    def serveGRPC(self, host):
        self.__grpcsServProc = Process(target=self._serveGRPC, args=(host,))
        self.__grpcsServProc.start()
    
    @classmethod
    def closeServers(self):
            self.__grpcsServProc.terminate()
        










     
if __name__ == '__main__':
    LocalAgent.serveGRPC()
