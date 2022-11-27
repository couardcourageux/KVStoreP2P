from dataclasses import dataclass, field, asdict
from typing import List, Dict

import json


class AgentDNodeHoster:
    agents = {}
    dnodes = {}
    
    @classmethod
    def show(self):
        print(AgentDNodeHoster.agents)
        print(AgentDNodeHoster.dnodes)
        
    # @classmethod
    # def find(self, truc:str):
    #     return self.agents.get(truc, None)


@dataclass
class Agent:
    agent_id: str
    ip: str
    port: str
    agent_type: int = -1
    capacity: int = 6000
    _hosting: str = ""
    
    
    def toDict(self) -> Dict:
        return asdict(self)
    
    @classmethod
    def fromDict(self, dict:Dict) -> 'Agent':
        ag = Agent(
            dict["agent_id"], 
            dict["ip"], 
            dict["port"],
            dict["agent_type"], 
            dict["capacity"], 
            dict["_hosting"]
        )
        return ag
    
    @classmethod
    def importFromDict(self, dict:Dict) -> str:
        ag = Agent.fromDict(dict)
        Agent.register(ag)
        return ag.agent_id
    
    # @property
    def hosting(self):
        if self._hosting == "":
            return None
        return DNode.get(self._hosting)
    
    def setHosting(self, node: 'DNode'):
        self._hosting = node.dNode_id
    
    def show(self):
        print(f"agent: {self.agent_id[:20]}, hosting node {DNode.get(self._hosting).dNode_id[:20]}")
        
    def getAddr(self) -> str:
        return self.ip + ":" + self.port
            
    @classmethod
    def register(self, agent:'Agent') -> None:
        AgentDNodeHoster.agents[agent.agent_id] = agent
            
    @classmethod
    def get(self, agent_id:str) -> 'Agent':
        return AgentDNodeHoster.agents.get(agent_id, None)
    
    @classmethod
    def unlist(self, agent_id:str) -> None:
        AgentDNodeHoster.agents.pop(agent_id, None)
    
    
    
@dataclass
class DNode:
    dNode_id: str
    _predecessor: str = field(default="", repr=False)
    _agents: List[str] = field(default_factory=list, repr=False)
    _fingerTable: List[str] = field(default_factory=list, repr=False)
    
    
    def toDict(self):
        dict = asdict(self)
        dict.pop("_fingerTable", None)
        ags = self.agents()
        for c in ags.keys():
            ags[c] = asdict(ags[c])
        dict["_agents"] = list(ags.values())
        return dict
    
    @classmethod
    def fromDict(self, dict:Dict) -> 'DNode':
        node = DNode(
            dict["dNode_id"], 
            dict["_predecessor"]
        )
        return node
    
    @classmethod
    def importFromDict(self, dict:Dict) -> str:
        print(dict)
        node = DNode.fromDict(dict)
        DNode.register(node)
        for dc in dict["_agents"]:
            ag_id = Agent.importFromDict(dc)
            node.addAgent(Agent.get(ag_id))
            
        return node.dNode_id
    
    ###################################
    @classmethod
    def register(self, dnode:'DNode') -> None:
        AgentDNodeHoster.dnodes[dnode.dNode_id] = dnode
            
    @classmethod
    def get(self, dNode_id:str) -> 'DNode':
        return AgentDNodeHoster.dnodes.get(dNode_id, None)
    
    @classmethod
    def unlist(self, dNode_id:str) -> None:
        AgentDNodeHoster.dnodes.pop(dNode_id, None)
    ###################################
    # @property
    def predecessor(self) -> 'DNode':
        if self._predecessor == "":
            return None
        return DNode.get(self._predecessor)
    
    def setPredecessor(self, node: 'DNode'):
        self._predecessor = node.dNode_id
    ###################################
    # @property
    def agents(self) -> Dict[str, 'Agent']:
        output = {x: Agent.get(x) for x in self._agents}
        output = {k: v for k, v in output.items() if v is not None}
        return output
    
    def addAgent(self, agent: 'Agent') -> None:
        if not agent.agent_id in self._agents:
            self._agents.append(agent.agent_id)
            
    def delAgent(self, agent_id: str) -> None:
        if agent_id in self._agents:
            self._agents.remove(agent_id)
            
    def clearAgents(self) -> None:
        self._agents.clear()
    ###################################
    
    
    
    
    # @property
    def fingerTable(self) -> Dict[str, 'DNode']:
        output = {x: Agent.get(x) for x in self._fingerTable}
        output = {k: v for k, v in output.items() if v is not None}
        return output
    
    
    
        
    





