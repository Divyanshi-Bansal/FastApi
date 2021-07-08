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