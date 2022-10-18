import sys
import os

LOCAL_DIRECTORY = os.getcwd()
sys.path.append(os.path.join(LOCAL_DIRECTORY, "pathsMethods"))
sys.path.append(os.path.join(LOCAL_DIRECTORY, "apiTypes"))
###

from fastapi import FastAPI

from apiReqInterpreter import ApiReqInterpret
from router import Router
from putRequests import SetEntry,SetEntries, DelGetEntry


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
