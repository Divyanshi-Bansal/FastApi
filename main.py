from fastapi import FastAPI
from typing import Optional
import uvicorn

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


@app.post('/blog')
def createBlog(request: Blog):
    return {'data':f"Blog is ceated {request}"}


# for debugging on another port
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1',port='8000')