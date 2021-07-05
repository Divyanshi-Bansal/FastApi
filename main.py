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
def show(id):
    return {'data': id}