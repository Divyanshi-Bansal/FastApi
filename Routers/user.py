from fastapi import APIRouter , Depends , HTTPException , status
from database import get_db
import models , schemas
from hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(
    tags='Usesr',
    prefix = '/user'
)


@router.post('/users' , tags=['Users'])
def createUser(request: schemas.User, db:Session = Depends(get_db)):
    hashedPwd = Hash.bcrypt(request.password)
    newUser = models.User(name = request.name , email = request.email , password = hashedPwd , contact = request.contact)
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser


@router.get('/users/{id}' , status_code=200 , response_model=schemas.ShowUser , tags=['Users'])
def showUser(id:int , db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"user with id {id} is not found.")

    return user


@router.put('/users/{id}' , tags=['Users'])
def updateUser(id:int ,request:schemas.User , db:Session = Depends(get_db)):
    newuser = db.query(models.User).filter(models.User.id == id)

    if not newuser.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"the user of id {id} is not found.")

    newuser.update(request)
    db.commit()
    return "updated successfully"


@router.delete('/user/{id}' , tags=['Users'])
def deleteUser(id:int , db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"user of id {id} is not found")

    user.delete(synchronize_session = False)
    db.commit()
    return "deleted successfully"
