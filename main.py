from fastapi import FastAPI , Depends , status , Response ,  HTTPException
from typing import Optional ,List , Dict
import uvicorn
import schemas
import models
from database import engine , SessionLocal
from sqlalchemy.orm import Session
from hashing import Hash


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


@app.get('/blog' , tags=['Blogs'])
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


@app.get('/blog/{id}' , status_code=200 , response_model=schemas.ShowBlog , tags=['Blogs'])
def show(id:int ,response:Response , db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Blog with id {id} is not present in database")

    return blog


# to add details
@app.post('/blog', status_code=status.HTTP_201_CREATED , tags=['Blogs'])
def createBlog(request: schemas.Blog , db:Session = Depends(get_db)):
    # return {'data':f"Blog is ceated {request}"}
    # newBlog is going to schemas
    newBlog = models.Blog(title = request.title , body = request.body , published=request.published , userId=1)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    return newBlog


@app.delete('/blog/{id}' , tags=['Blogs'])
def blogDelete(id:int , db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} is not found.")

    blog.delete(synchronize_session = False)
    db.commit()
    return {"detail":f"successfully delete blog with id {id}"}


@app.put('/blog/{id}' , status_code=status.HTTP_202_ACCEPTED , tags=['Blogs'])
def blogUpdate(id:int , request:schemas.Blog , db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"blog with id {id} is not found.")

    blog.update(request)
    db.commit()
    return "updated"




@app.post('/users' , tags=['Users'])
def createUser(request: schemas.User, db:Session = Depends(get_db)):
    hashedPwd = Hash.bcrypt(request.password)
    newUser = models.User(name = request.name , email = request.email , password = hashedPwd , contact = request.contact)
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser


@app.get('/users/{id}' , status_code=200 , response_model=schemas.ShowUser , tags=['Users'])
def showUser(id:int , db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"user with id {id} is not found.")

    return user


@app.put('/users/{id}' , tags=['Users'])
def updateUser(id:int ,request:schemas.User , db:Session = Depends(get_db)):
    newuser = db.query(models.User).filter(models.User.id == id)

    if not newuser.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"the user of id {id} is not found.")

    newuser.update(request)
    db.commit()
    return "updated successfully"


@app.delete('/user/{id}' , tags=['Users'])
def deleteUser(id:int , db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"user of id {id} is not found")

    user.delete(synchronize_session = False)
    db.commit()
    return "deleted successfully"


# for debugging on another port
# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1',port='8000')