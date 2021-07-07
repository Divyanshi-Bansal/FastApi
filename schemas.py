from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):

    title: str
    body: str
    published: Optional[bool]


class User(BaseModel):
    name:str
    email:str
    password:str
    contact:int


class ShowUser(BaseModel):

    name:str
    email:str
    contact:int

    class Config():
        orm_mode =True


class ShowBlog(BaseModel):

    title:str
    body:str
    creator:ShowUser
    published:Optional[bool]

    class Config():
        orm_mode= True
