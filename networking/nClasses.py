from dataclasses import dataclass, field
from typing import List, Dict





@dataclass
class Agent:
    agent_id: str
    ip: str
    port: str
    hosting: Dict[str, 'DNode'] = field(default_factory=dict, repr=False)
    
    
    
@dataclass
class DNode:
    dNode_id: str
    predecessor: 'DNode' = field(repr=False)
    agents: Dict[str,   'Agent'] = field(default_factory=dict, repr=False)
    fingerTable: Dict[str, 'DNode'] = field(default_factory=dict, repr=False)
    
    
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
    