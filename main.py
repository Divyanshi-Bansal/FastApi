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






# for debugging on another port
# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1',port='8000')