from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/blog')
def index(limit):
    return {'data':f'{limit} blogs from the database'}

@app.get('/about')
def about():
    return {'data':'about blog page'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'unpublished blog data here'}


@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id:int):
    return {'data':{id:'comments on blog'}}