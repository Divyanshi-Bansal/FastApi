from fastapi import APIRouter , Depends , HTTPException , status
from database import get_db
import models , schemas , oauth2
from sqlalchemy.orm import Session
from Repository import blog

router = APIRouter(
    tags=['Blogs'],
    prefix = '/blog'
)


@router.get('/')
def showAll(db:Session = Depends(get_db) , current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.getAll(db)

@router.get('/{id}')
def showBlogId(id:int , db:Session = Depends(get_db) , current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.getBlogId(id , db)

@router.post('/')
def createBlog(request:schemas.Blog , db:Session = Depends(get_db) , current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.createBlog(request , db)


@router.delete('/blog/{id}')
def blogDelete(id:int , db:Session = Depends(get_db) , current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.blogDelete(id , db)


@router.put('/blog/{id}' , status_code=status.HTTP_202_ACCEPTED)
def blogUpdate(id:int , request:schemas.Blog , db:Session = Depends(get_db) , current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.blogUpdate(id , request , db)
