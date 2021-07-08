from pydantic import BaseModel
from typing import Optional , List

class Blog(BaseModel):

    title: str
    body: str
    published: Optional[bool]

    class Config():
        orm_mode = True


class User(BaseModel):
    name:str
    email:str
    password:str
    contact:int

    class Config():
        orm_mode  = True


class ShowUser(BaseModel):

    name:str
    email:str
    contact:int
    blogs: List[Blog] = []

    class Config():
        orm_mode = True


class ShowBlog(BaseModel):

    title:str
    body:str
    creator:User
    published:Optional[bool]

    class Config():
        orm_mode= True


class login(BaseModel):
    name:str
    email:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None