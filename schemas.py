from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):

    id:int
    name: str
    title: str
    body: str
    published: Optional[bool]

class ShowBlog(Blog):
    name:str
    title:str
    published:Optional[bool]
