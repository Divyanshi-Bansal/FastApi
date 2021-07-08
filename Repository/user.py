import models
from fastapi import HTTPException , status
from hashing import Hash



def createUser(request, db):
    hashedPwd = Hash.bcrypt(request.password)
    newUser = models.User(name = request.name , email = request.email , password = hashedPwd , contact = request.contact)
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser

def showUser(id, db):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"user with id {id} is not found.")

    return user

def updateUser(id ,request, db):
    newuser = db.query(models.User).filter(models.User.id == id)

    if not newuser.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"the user of id {id} is not found.")

    newuser.update(request)
    db.commit()
    return "updated successfully"

def deleteUser(id, db):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"user of id {id} is not found")

    user.delete(synchronize_session = False)
    db.commit()
    return "deleted successfully"