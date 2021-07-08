from fastapi import APIRouter , Depends , HTTPException , status
from database import get_db
import models , schemas , hashing
from sqlalchemy.orm import Session

router = APIRouter(
    tags='Blogs',
    prefix = '/blog'
)


@router.get('/')
def showAll(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.get('/{id}')
def showBlogId(id:int , db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"the blog with id {id} is not present.")

    return blog

@router.post('/')
def createBlog(request:schemas.Blog , db:Session = Depends(get_db)):
    newBlog = models.Blog(title=request.title, body=request.body, published=request.published, userId=1)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    return newBlog


@router.delete('/blog/{id}' , tags=['Blogs'])
def blogDelete(id:int , db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} is not found.")

    blog.delete(synchronize_session = False)
    db.commit()
    return {"detail":f"successfully delete blog with id {id}"}


@router.put('/blog/{id}' , status_code=status.HTTP_202_ACCEPTED , tags=['Blogs'])
def blogUpdate(id:int , request:schemas.Blog , db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"blog with id {id} is not found.")

    blog.update(request)
    db.commit()
    return "updated"
