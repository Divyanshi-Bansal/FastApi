from fastapi import APIRouter , Depends , HTTPException , status
from database import get_db
import models , schemas
from sqlalchemy.orm import Session
from repository import blog

router = APIRouter(
    tags=['Blogs'],
    prefix = '/blog'
)


@router.get('/')
def showAll(db:Session = Depends(get_db)):
    return blog.getAll(db)

@router.get('/{id}')
def showBlogId(id:int , db:Session = Depends(get_db)):
    return blog.getBlogId(id , db)

@router.post('/')
def createBlog(request:schemas.Blog , db:Session = Depends(get_db)):
    return blog.createBlog(request , db)


@router.delete('/blog/{id}')
def blogDelete(id:int , db:Session = Depends(get_db)):
    return blog.blogDelete(id , db)


@router.put('/blog/{id}' , status_code=status.HTTP_202_ACCEPTED)
def blogUpdate(id:int , request:schemas.Blog , db:Session = Depends(get_db)):
    return blog.blogUpdate(id , request , db)
