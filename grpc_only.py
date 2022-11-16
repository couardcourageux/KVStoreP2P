import sys
import os

LOCAL_DIRECTORY = os.getcwd()
GRPC_DIR = os.path.join(LOCAL_DIRECTORY, "grpc")


sys.path.append(os.path.join(LOCAL_DIRECTORY, "networking"))
sys.path.append(GRPC_DIR)

import argparse
from localAgent import LocalAgent
from grpc_server import get_server



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gport', type=str, required=True)
    parser.add_argument('--join', type=str, required=False)
    
    args = parser.parse_args()
    
    if args.join:
        LocalAgent.confAgent("localhost", args.gport, 6000)
        LocalAgent.joinNetwork(args.join)
        # LocalAgent.showMe()
        # print(LocalAgent.__agent)
    else:
        LocalAgent.confAgent("localhost", args.gport, 6000)
        LocalAgent.initNetwork()
        LocalAgent.showMe()
        # si j'ai un doute sur peut-on travailler sur l'agent retourné
        # LocalAgent.getAgent().hosting.dNode_id = "chips"
        # LocalAgent.showMe()

    server = get_server("localhost:{}".format(args.gport))
    server.start()
    server.wait_for_termination()