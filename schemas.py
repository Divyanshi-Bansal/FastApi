from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):

    id:int
    name: str
    title: str
    body: str
    published: Optional[bool]

class ShowBlog(BaseModel):

    name:str
    title:str
    published:Optional[bool]

    class Config():
        orm_mode= True


class ShowUser(BaseModel):
    name:str
    email:str
    password:str
    contact:int
