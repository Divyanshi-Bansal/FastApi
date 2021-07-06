from sqlalchemy import Column , Integer , String , BOOLEAN
from database import Base

class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer , primary_key=True , index=True)
    name = Column(String)
    title = Column(String)
    body = Column(String)
    published = Column(BOOLEAN)
