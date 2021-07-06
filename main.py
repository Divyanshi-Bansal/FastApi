from fastapi import FastAPI , Depends , status , Response ,  HTTPException
from typing import Optional ,List
import uvicorn
import schemas
import models
from database import engine , SessionLocal
from sqlalchemy.orm import Session


# from .schemas import Blog

app = FastAPI()

models.Base.metadata.create_all(engine)




def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close



@app.get('/')
def index(limit=10,published:bool=True,sort:Optional[str]=None): #here we define the default value of limit and published
    # return (published)
    if published:
        return {'data':f'{limit} blogs from the database'}
    else:
        return {'data' : 'not published yet'}


@app.get('/blog')
def allBlogs(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

# @app.get('/about')
# def about():
#     return {'data':'about blog page'}
#
# @app.get('/blog/unpublished')
# def unpublished():
#     return {'data':'unpublished blog data here'}


@app.get('/blog/{id}' , status_code=200 , response_model=schemas.ShowBlog)
def show(id:int ,response:Response , db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Blog with id {id} is not present in database")

    return blog


# to add details
@app.post('/blog', status_code=status.HTTP_201_CREATED)
def createBlog(request: schemas.Blog , db:Session = Depends(get_db)):
    # return {'data':f"Blog is ceated {request}"}
    # newBlog is going to schemas
    newBlog = models.Blog(id = request.id , title = request.title , body = request.body , name = request.name, published=request.published)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    return newBlog


@app.delete('/blog/{id}')
def blogDelete(id:int , db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} is not found.")

    blog.delete(synchronize_session = False)
    db.commit()
    return {"detail":f"successfully delete blog with id {id}"}


@app.put('/blog/{id}' , status_code=status.HTTP_202_ACCEPTED)
def blogUpdate(id:int , request:schemas.Blog , db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"blog with id {id} is not found.")

    blog.update(request)
    db.commit()
    return "updated"


@app.post('/users')
def createUser(request: schemas.ShowUser, db:Session = Depends(get_db)):
    newUser = models.User(name = request.name , email = request.email , password = request.password , contact = request.contact)
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser



# for debugging on another port
# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1',port='8000')