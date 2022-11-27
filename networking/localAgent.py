import sys
import os

LOCAL_DIRECTORY = os.getcwd()
GRPC_DIR = os.path.join(LOCAL_DIRECTORY, "grpc")

sys.path.append(GRPC_DIR)
sys.path.append(os.path.join(GRPC_DIR, "pyProtos"))
sys.path.append(os.path.join(GRPC_DIR, "clients"))

sys.path.append(os.path.join(LOCAL_DIRECTORY, "cronJobs"))


from agent_and_dnode import Agent, DNode
from utilitary import create_agent_id, create_node_id
from ringClient import RingClient
from clusterClient import ClusterClient

from clusterMaster import ClusterMaster
from clusterSlave import ClusterSlave
from initExecutor import InitExecutor

class LocalAgent:
    __agent = ""
    __grpcServer = None
    __clusterMaster = None
    __clusterSlave = None
    __initExecutor = None
    __tamponMem = {}
    
    
    @classmethod
    def createCrons(self):
        self.__clusterMaster = ClusterMaster(self.__port)
        self.__clusterSlave = ClusterSlave(self.__port)
        self.__initExecutor = InitExecutor(self.__port)
        
    @classmethod
    def setMemData(self, key:str, val):
        self.__tamponMem[key] = val

    @classmethod
    def getMemData(self, key:str):
        return self.__tamponMem.get(key, None)    
    
    @classmethod
    def getAgent(self) -> Agent:
        return Agent.get(self.__agent)
    
    
    @classmethod
    def initAgent(self):
        ag = Agent("need init", "localhost", "00")
        Agent.register(ag)
        self.__agent = ag.agent_id
        
    @classmethod
    def initNetwork(self):
        agent = Agent.get(self.__agent)
        agent.agent_id = create_agent_id()
        Agent.register(agent)
        self.__agent = agent.agent_id
        
        dNode = DNode(create_node_id(), None, [self.__agent])
        DNode.register(dNode)
        agent.setHosting(dNode)
        agent.setHosting(dNode)
        
        
    @classmethod
    def confAgent(self, ip:str, port:str, capacity:int) -> None:
        agent = Agent.get(self.__agent)
        agent.ip = ip
        agent.port = port
        agent.capacity = capacity
        
    @classmethod
    def showMe(self):
        Agent.get(self.__agent).show()
        
    @classmethod
    def joinNetwork(self, distantAgentHost: str):
        agent_id, node_id = RingClient.join_network(distantAgentHost)
        agent = LocalAgent.getAgent()
        agent.agent_id = agent_id
        
        dict = RingClient.searchAddr(distantAgentHost, node_id)
        # la description du Node qu'on cherche à joindre
        
        # DNode.importFromDict(dict)
        
        truc = ClusterClient.joinNode(distantAgentHost, self.getAgent())
        
        print(f"joining network as : agent_id: {agent_id[:20]}")
        print(f"will request for adress of {node_id[:20]}")
        
        print(truc)