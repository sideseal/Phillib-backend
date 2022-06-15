#!/usr/bin/env python3

###################
#  python 3.7.10  #
###################

import uvicorn
from fastapi import FastAPI
from database import startup
from controller import get_all_articles


APP_HOST_ADDRESS = "0.0.0.0"
APP_PORT = 8000

app = FastAPI()

@app.get("/")
def show_all_articles():
    return {"articles": get_all_articles()}

@app.get("/test/{test_id}")
def test_get(test_id : int):
    return {"test_id": test_id}

#def serve():
#    uvicorn.run(app, host=APP_HOST_ADDRESS, port=APP_PORT)

if __name__=="__main__":
    startup()
    uvicorn.run("server:app",
                host=APP_HOST_ADDRESS,
                port=APP_PORT,
                reload=True,
                )
