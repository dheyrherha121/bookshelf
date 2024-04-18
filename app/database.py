from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import setting

SQLALCHEMY_DATABASE_URL = f'postgresql://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
sesionLocal = sessionmaker(autoflush=False, autocommit = False, bind = engine)
Base = declarative_base()

def get_db():
    db = sesionLocal()
    try:
        yield db
    finally:
        db.close()