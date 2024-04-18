from .database import Base
from sqlalchemy import Column, Integer,String,VARCHAR, Date
class Books(Base):
    __tablename__ = 'AddedBooks'
    
    id = Column(Integer, primary_key=True, nullable= False)
    title = Column(String, nullable= False)
    ISBN = Column(Integer, nullable=False)
    Author = Column(VARCHAR, nullable=False)