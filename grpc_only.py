import sys
import os



LOCAL_DIRECTORY = os.getcwd()
GRPC_DIR = os.path.join(LOCAL_DIRECTORY, "grpc")


sys.path.append(os.path.join(LOCAL_DIRECTORY, "networking"))
sys.path.append(GRPC_DIR)

import argparse
from localAgent import LocalAgent
from grpc_server import get_server
from agent_and_dnode import AgentDNodeHoster, Agent, DNode
from utilitary import create_node_id

from dataclasses import asdict



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gport', type=str, required=True)
    parser.add_argument('--join', type=str, required=False)
    
    args = parser.parse_args()
    argz = {
        "join":args.join,
        "gport":args.gport
    }
    
    LocalAgent.setMemData("args", argz)
    LocalAgent.createCrons(args.gport)
    LocalAgent.launchCron("init")
    
   

    server = get_server("0.0.0.0:{}".format(args.gport))
    server.start()
    server.wait_for_termination()