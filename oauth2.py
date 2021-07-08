from fastapi import Depends , HTTPException , status
from fastapi.security import OAuth2PasswordBearer
import tokens

import schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'token')

def get_current_user(token:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code= status.HTTP_401_UNAUTHORIZED , detail="could not validate credentials" , headers={"WWW-Authenticate":"Bearer"})
    return tokens.verify_token(token , credentials_exception)
