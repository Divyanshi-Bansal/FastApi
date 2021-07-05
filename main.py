from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index(limit=10,published:bool=True,sort:Optional[str]=None): #here we define the default value of limit and published
    # return (published)
    if published:
        return {'data':f'{limit} blogs from the database'}
    else:
        return {'data' : 'not published yet'}

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


# to get data from user that add in our api, we need BaseModel for this
class Blog(BaseModel):
    title: str
    body: str
    name : str
    published: Optional[bool]

@app.post('/blog')
def createBlog(request: Blog):
    return {'data':"Blog is ceated"}