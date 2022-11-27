import sys
import os

LOCAL_DIRECTORY = os.getcwd()
GRPC_DIR = os.path.join(LOCAL_DIRECTORY, "grpc")


sys.path.append(os.path.join(LOCAL_DIRECTORY, "networking"))
sys.path.append(os.path.join(GRPC_DIR, "pyProtos"))


import ring_pb2
import ring_pb2_grpc
import json
from localAgent import LocalAgent


class NetworkCronServicer(ring_pb2_grpc.NetworkCronJobServicer):
    def callInitAgent(self, request, context) -> ring_pb2.voidMsg:
        args = json.loads(request.theString)
        
        if args["join"]:
            LocalAgent.initAgent()
            LocalAgent.confAgent("localhost", args["gport"], 6000)
            LocalAgent.joinNetwork(args["join"])
        # LocalAgent.showMe()
        # print(LocalAgent.__agent)
        else:
            LocalAgent.initAgent()
            LocalAgent.confAgent("localhost", args["gport"], 6000)
            # AgentDNodeHoster.show()
        
            LocalAgent.initNetwork()
            # LocalAgent.showMe()
            # print(LocalAgent.getAgent().toDict())
            ag = LocalAgent.getAgent()
            node = ag.hosting()
        
        
        