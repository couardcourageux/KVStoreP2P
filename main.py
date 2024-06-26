import sys
import os

LOCAL_DIRECTORY = os.getcwd()
WEB_SERVICE = os.path.join(LOCAL_DIRECTORY, "webService")

sys.path.append(os.path.join(WEB_SERVICE, "pathsMethods"))
sys.path.append(os.path.join(WEB_SERVICE, "apiTypes"))
sys.path.append(os.path.join(LOCAL_DIRECTORY, "networking"))
###
import uvicorn
import argparse


from fastapi import FastAPI

from webService.apiReqInterpreter import ApiReqInterpret
from router import Router
from putRequests import SetEntry,SetEntries, DelGetEntry
from localAgent import LocalAgent



app = FastAPI()
@app.get("/")
async def read_root():
    return Router.main()

@app.post("/putEntry")
async def putEntry(req: SetEntry):
    resp = Router.setEntry(ApiReqInterpret.processPutEntry(req))
    return resp

@app.post("/putEntries")
async def putEntries(req: SetEntries):
    resp = Router.setEntries(ApiReqInterpret.processPutEntries(req))
    return resp

@app.post("/getEntry")
async def getEntry(req: DelGetEntry):
    return Router.getEntry(ApiReqInterpret.processDelGetEntry(req))

@app.delete("/delEntry")
async def delEntry(req: DelGetEntry):
    return Router.delEntry(ApiReqInterpret.processDelGetEntry(req))


@app.on_event('shutdown')
def shutdown_event():
    LocalAgent.closeServers()
    
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--aport', type=int, required=True)
    parser.add_argument('--gport', type=str, required=True)
    parser.add_argument('--join', type=str, required=False)
    
    args = parser.parse_args()
        
    
    if args.join:
        LocalAgent.joinNetwork(args.join)
        # print(LocalAgent.__agent)
    else:
        LocalAgent.initNetwork(args.gport)
        LocalAgent.showMe()
    
    host = "localhost:{}".format(args.gport)
    LocalAgent.serveGRPC(host)
    
    uvicorn.run("main:app", host="0.0.0.0", port=args.aport, reload=True)