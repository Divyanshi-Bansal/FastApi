from fastapi import APIRouter , Depends , HTTPException , status
from database import get_db
import schemas
from Repository import user
from sqlalchemy.orm import Session

router = APIRouter(
    tags=['Usesr'],
    prefix = '/user'
)


@router.post('/')
def createUser(request: schemas.User, db:Session = Depends(get_db)):
    return user.createUser(request , db)


@router.get('/{id}' , status_code=200 , response_model=schemas.ShowUser)
def showUser(id:int , db:Session = Depends(get_db)):
    return user.showUser(id , db)


@router.put('/{id}')
def updateUser(id:int ,request:schemas.User , db:Session = Depends(get_db)):
    return user.updateUser(id , request , db)


@router.delete('/{id}')
def deleteUser(id:int , db:Session = Depends(get_db)):
    return user.deleteUser(id , db)
