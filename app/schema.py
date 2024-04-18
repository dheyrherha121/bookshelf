from pydantic import BaseModel, ConfigDict


class BooksIn(BaseModel):
    title: str
    Author: str
    ISBN: int
    

class BookOut(BaseModel):
    title: str
    Author: str
    ISBN: int
    
