import models
from fastapi import HTTPException , status



def getAll(db):
    blogs = db.query(models.Blog).all()
    return blogs

def getBlogId(id, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"the blog with id {id} is not present.")

    return blog


def createBlog(request , db):
    newBlog = models.Blog(title=request.title, body=request.body, published=request.published, userId=1)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    return newBlog

def blogDelete(id, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} is not found.")

    blog.delete(synchronize_session = False)
    db.commit()
    return {"detail":f"successfully delete blog with id {id}"}

def blogUpdate(id, request, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"blog with id {id} is not found.")

    blog.update(request)
    db.commit()
    return "updated"
