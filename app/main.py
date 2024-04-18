from fastapi import FastAPI
from . import crud


app = FastAPI()
app.include_router(crud.router)

@app.get('/')
def welcome():
    return {'welcome to our bookshelf api, here we help you store your books into an organized database where you can do anything you want with it. THANKS.'}
