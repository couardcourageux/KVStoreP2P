import sys
import os

LOCAL_DIRECTORY = os.getcwd()
GRPC_DIR = os.path.join(LOCAL_DIRECTORY, "grpc")


sys.path.append(os.path.join(GRPC_DIR, "clients"))

from clusterClient import ClusterClient

from agent_and_dnode import Agent, DNode
from localAgent import LocalAgent
from typing import Dict
import asyncio

import json

def joiningClusterProc(agentDict:str) -> Dict[bool, str]:
    dNode = LocalAgent.getAgent().hosting()
    
    joiningAgent_id = Agent.importFromDict(json.loads(agentDict))
    joiningAgent = Agent.get(joiningAgent_id)
    
    joiningAgent.setHosting(dNode)
    Agent.register(joiningAgent)
    dNode.addAgent(joiningAgent)
    print(LocalAgent.getAgent().hosting().toDict())
    updateNodeDataOnCluster()
    stability()
    updateNodeDataOnCluster()
        
    
    return {
        "accepted":True, 
        "NodeDict": json.dumps(dNode.toDict())
    }
    
def updateNodeDataOnCluster() -> None:
    lag = LocalAgent.getAgent()
    dNode = lag.hosting()

    nodeDict = json.dumps(dNode.toDict())
    ags = dNode.agents()
    for c, ag in ags.items():
        if c != lag.agent_id:
            ClusterClient.sendUpdateNodeData(ag.getAddr(), nodeDict)
            
def stability():
    pass
    