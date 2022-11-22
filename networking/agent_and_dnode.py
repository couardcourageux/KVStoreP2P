from dataclasses import dataclass, field
from typing import List, Dict

import json



@dataclass
class Agent:
    agent_id: str
    ip: str
    port: str
    agent_type: int = -1
    capacity: int = 6000
    hosting: 'DNode' | str = None
    
    def show(self):
        print(f"agent: {self.agent_id[:20]}, hosting node {self.hosting.dNode_id[:20]}")
        
    def get_identity(self):
        dict = {
            "agent_id": self.agent_id,
            "ip": self.ip,
            "port":self.port,
            "type": self.agent_type,
            "capacity": self.capacity,
        }
        if self.hosting != None:
            dict["hosting_id"] = self.hosting.dNode_id
        else:
            dict["hosting_id"] = ""
        
        return dict
    
    def export_identity(self):
        return json.dumps(self.get_identity())
    
    @classmethod
    def import_identity(self, identity:str) -> 'Agent':
        # dict = json.loads(identityStr)
        agent = Agent(identity["agent_id"], identity["ip"], identity["port"], identity["type"], identity["capacity"], identity["hosting_id"])
        return agent
    
    
    
@dataclass
class DNode:
    dNode_id: str
    predecessor: 'DNode' | str = field(repr=False)
    agents: Dict[str, 'Agent'] = field(default_factory=dict, repr=False)
    fingerTable: Dict[str, 'DNode'] = field(default_factory=dict, repr=False)
    
    def get_identity(self) -> Dict:
        dict = {
            'nodeId': self.dNode_id,
            'agents': [x.get_identity() for x in self.agents],
            'predecessor_id': ""
        }
        
        if self.predecessor != None:
            dict['predecessor_id'] = self.predecessor.dNode_id
        
        return dict
    
    def export_identity(self) -> str:
        return json.dumps(self.get_identity())
    
    @classmethod
    def getNodeFromIdentity(self, identityStr: str) -> 'DNode':
        dict = json.loads(identityStr)
        
        node = DNode(   dict['nodeId'], 
                        dict["predecessor_id"], 
                        {x["agent_id"]:Agent.import_identity(x) for x in dict["agents"] }
                    )
        
        # for c, v in node.agents.item():
        #     v.
        
    












  
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
    