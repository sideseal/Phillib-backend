#!/usr/bin/env python3

###################
#  python 3.7.10  #
###################

import uvicorn
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import startup
from controller import get_all_articles

PATH = os.environ["HOME"]
APP_HOST_ADDRESS = "0.0.0.0"
APP_PORT = 8000

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def show_all_articles():
    return {"articles": get_all_articles()}

@app.get("/test/{test_id}")
def test_get(test_id: int):
    return {"test_id": test_id}

#def serve():
#    uvicorn.run(app, host=APP_HOST_ADDRESS, port=APP_PORT)

if __name__=="__main__":
    startup()
    uvicorn.run("server:app",
                host=APP_HOST_ADDRESS,
                port=APP_PORT,
                # reload=True,
                # ssl_keyfile="/etc/letsencrypt/live/api.phillib.com/privkey.pem",
                # ssl_certfile="/etc/letsencrypt/live/api.phillib.com/fullchain.pem",
                )
