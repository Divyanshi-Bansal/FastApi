from fastapi import APIRouter
import schemas , models , tokens
from hashing import Hash
from sqlalchemy.orm import Session
from fastapi import Depends , HTTPException , status
from database import get_db


router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:schemas.login , db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="invalid email")

    if not Hash.verifyPwd(user.password , request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="invalid password")

    access_token = tokens.create_access_token(data={"sub":user.email})

    return {"access_token": access_token , "token_type":"bearer"}