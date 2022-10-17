from fastapi import FastAPI
# from multiprocessing import Manager

from globalDetainer import GlobalDetainer



app = FastAPI()
@app.get("/")
async def read_root():
    return GlobalDetainer.main()

@app.get("/init")
async def read_root():
    return GlobalDetainer.initial()

@app.get("/sec")
async def read_root():
    return GlobalDetainer.secondStep()

@app.get("/get")
async def read_root():
    return GlobalDetainer.getEntries()

@app.get("/del")
async def read_root():
    return GlobalDetainer.deleteEntries()