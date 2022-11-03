from dataclasses import dataclass, field
from typing import List, Dict





@dataclass
class Agent:
    agent_id: str
    ip: str
    port: str
    hosting: Dict[str, 'DNode'] = field(default_factory=list)
    
    
    
@dataclass
class DNode:
    dNode_id: str
    predecessor: 'Agent'
    agents: List['Agent'] = field(default_factory=list)
    fingerTable: Dict[str, 'DNode'] = field(default_factory=dict)
    