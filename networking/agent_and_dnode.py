from dataclasses import dataclass, field
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
    
    # @property
    def hosting(self):
        if self._hosting == "":
            return None
        return DNode.get(self._hosting)
    
    def setHosting(self, node: 'DNode'):
        self._hosting = node.dNode_id
    
    def show(self):
        print(f"agent: {self.agent_id[:20]}, hosting node {DNode.get(self._hosting).dNode_id[:20]}")
        
            
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
            
    def delAgent(self, agent: 'Agent') -> None:
        if agent.agent_id in self._agents:
            self._agents.remove(agent.agent_id)
            
    def clearAgents(self) -> None:
        self._agents.clear()
    ###################################
    
    
    
    
    # @property
    def fingerTable(self) -> Dict[str, 'DNode']:
        output = {x: Agent.get(x) for x in self._fingerTable}
        output = {k: v for k, v in output.items() if v is not None}
        return output
    
    
    
        
    












  
if __name__ == '__main__':
    a1 = Agent("a1", "host", "00")
    a2 = Agent("a2", "host", "00")
    a3 = Agent("a3", "host", "00")
    a4 = Agent("a4", "host", "00")
    a5 = Agent("a5", "host", "00")
    
    d1 = DNode("d1", None, [a1, a2, a3])
    
    host_base = {"d1": d1}
    a1.hosting = host_base.copy()
    a2.hosting = host_base.copy()
    a3.hosting = host_base.copy()
    
    print(a1.hosting, d1.agents)
    