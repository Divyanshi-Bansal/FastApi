from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'

# represent the core interface to the database
engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={"check_same_thread":False})

SessionLocal =  sessionmaker(bind=engine , autocommit=False , autoflush=False)

# allow us to create classes that include directives to describe the actual database table they will be mapped to.
Base = declarative_base()