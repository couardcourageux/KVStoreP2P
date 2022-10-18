import sys
import os

LOCAL_DIRECTORY = os.getcwd()
sys.path.append(os.path.join(LOCAL_DIRECTORY, "pathsMethods"))
###

from fastapi import FastAPI

from router import Router


app = FastAPI()
@app.get("/")
async def read_root():
    return Router.main()

@app.get("/init")
async def read_root():
    return Router.initial()

@app.get("/sec")
async def read_root():
    return Router.secondStep()

@app.get("/get")
async def read_root():
    return Router.getEntries()

@app.get("/del")
async def read_root():
    return Router.deleteEntries()