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
    def _setAgent(self, id:str, port:str="00", ip:str="localhost"):
        self.__agent.agent_id = id
        self.__agent.ip = ip
        self.__agent.port = port
        
    @classmethod
    def initNetwork(self):
        agent = self.getAgent()
        agent.agent_id = create_agent_id()
        dNode = DNode(create_node_id(), None, [self.__agent])
        dNode.predecessor = dNode
        self.__agent.hosting = dNode
        
    @classmethod
    def confAgent(self, ip:str, port:str, capacity:int) -> None:
        agent = self.getAgent()
        agent.ip = ip
        agent.port = port
        agent.capacity = capacity
        
    @classmethod
    def showMe(self):
        self.__agent.show()
        
    @classmethod
    def joinNetwork(self, distantAgentHost: str):
        agent_id, node_id = RingClient.join_network(distantAgentHost)
        agent = LocalAgent.getAgent()
        agent.agent_id = agent_id
        
        dict = RingClient.searchAddr(distantAgentHost, node_id)
        agents = []
        node = DNode(   node_id, 
                        None,
                        [],
                        []
                     )
        if dict["master"]["agentId"] != "":
            agents.append(  Agent(dict["master"]["agentId"], 
                                  dict["master"]["ip"], 
                                  dict["master"]["port"], 
                                  1,
                                  None,
                                  node
                        ))
        
        if dict["backup"]["agentId"] != "":
            agents.append(  Agent(dict["backup"]["agentId"], 
                                  dict["backup"]["ip"], 
                                  dict["backup"]["port"], 
                                  1,
                                  None,
                                  node
                        ))
        
        node.agents = agents
        
        RingClient.joinNode(distantAgentHost, agent.agent_id, agent.ip, agent.port)
        
        print(f"joining network: agent_id: {agent_id[:20]}")
        print(f"will request for adress of {node_id[:20]}")
        
        # agent.hosting = node
        # node.agents.append(agent)