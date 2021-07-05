from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':"Divyanshi"}}

@app.get('/about')
def about():
    return {'data':'about page'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'unpublished data here'}


@app.get('/blog/{id}/comments')
def comments(id:int):
    return {'data':{id:'comments'}}