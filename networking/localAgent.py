import sys
import os

LOCAL_DIRECTORY = os.getcwd()
GRPC_DIR = os.path.join(LOCAL_DIRECTORY, "grpc")

sys.path.append(GRPC_DIR)
sys.path.append(os.path.join(GRPC_DIR, "pyProtos"))
sys.path.append(os.path.join(GRPC_DIR, "clients"))


from agent_and_dnode import Agent, DNode
from utilitary import create_agent_id, create_node_id
from ringClient import RingClient

class LocalAgent:
    __agent = Agent("need init", "localhost", "00")
    __grpcServer = None
    
    @classmethod
    def getAgent(self) -> Agent:
        return self.__agent
    
    
    @classmethod
    def _setAgent(self, id:str, port:str, ip:str="localhost"):
        self.__agent.agent_id = id
        self.__agent.ip = ip
        self.__agent.port = port
        
    @classmethod
    def initNetwork(self, port: str):
        self._setAgent(create_agent_id(), port)
        dNode = DNode(create_node_id(), None, [self.__agent])
        dNode.predecessor = dNode
        self.__agent.hosting = dNode
        
    @classmethod
    def confAgent(self, ip:str, port:str, capacity:int, agent_type:int) -> None:
        agent = self.getAgent()
        agent.ip = ip
        agent.port = port
        agent.agent_type = agent_type
        agent.capacity = capacity
        
    @classmethod
    def showMe(self):
        self.__agent.show()
        
    @classmethod
    def joinNetwork(self, distantAgentHost: str):
        agent_id, node_id = RingClient.join_network(distantAgentHost)
        print(f"joining network: agent_id: {agent_id[:20]}")
        print(f"will request for adress of {node_id[:20]}")
        self.__agent.agent_id = agent_id