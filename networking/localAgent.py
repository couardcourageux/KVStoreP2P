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
from clusterClient import ClusterClient

class LocalAgent:
    __agent = ""
    __grpcServer = None
    
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
        agents = []
        node = DNode(   node_id, 
                        None,
                        [],
                        []
                     )
        if dict["master"]["agentId"] != "":
            ag1 =  Agent(dict["master"]["agentId"], 
                                  dict["master"]["ip"], 
                                  dict["master"]["port"], 
                                  1,
                                  None,
                                  node
                        )
            Agent.register(ag1)
            agents.append(ag1.agent_id)
        
        if dict["backup"]["agentId"] != "":
            ag2 = Agent(dict["backup"]["agentId"], 
                                  dict["backup"]["ip"], 
                                  dict["backup"]["port"], 
                                  1,
                                  None,
                                  node
                        )
            Agent.register(ag2)
            agents.append(ag2.agent_id)
        
        node.agents = agents
        DNode.register(node)
        
        ClusterClient.joinNode(distantAgentHost, self.getAgent())
        
        print(f"joining network: agent_id: {agent_id[:20]}")
        print(f"will request for adress of {node_id[:20]}")
        
        # agent.hosting = node
        # node.agents.append(agent)