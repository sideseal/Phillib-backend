#!/usr/bin/env python3

###################
#  python 3.7.10  #
###################

from fastapi import FastAPI
from controller import get_all_articles


app = FastAPI()

@app.get("/")
def show_all_articles():
    return {"articles": get_all_articles()}

