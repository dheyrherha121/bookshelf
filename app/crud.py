from fastapi import APIRouter, Depends, HTTPException,status
from . import schema, database, model
from sqlalchemy.orm import session
from typing import List


router = APIRouter(
    tags= ['books'],
    prefix= '/books'
)

@router.post('/', response_model=List[schema.BookOut])
def create_book(book: schema.BooksIn, db: session= Depends(database.get_db)):
    new_book = model.Books(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return {new_book}

@router.get('/')
def get_all_books(id: int, db: session = Depends(database.get_db)):
    books = db.query(model.Books).filter(model.Books.id == id).first()
    return {books}

@router.delete('/')
def delete_book(id: int, db: session = Depends(database.get_db)):
    DeletedOne = db.query(model.Books).filter(model.Books.id == id)
    finalePost = DeletedOne.first()
    if finalePost == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= 'The post you want to delete is not found')
    DeletedOne.delete(synchronize_session = False)
    db.commit()
    return {'The book is succesfully deleted'}

@router.put('/')
def update_Books(id: int, book: schema.BooksIn, db: session = Depends(database.get_db)):
    update_one = db.query(model.Books).filter(model.Books.id == id)
    final_update = update_one.first()
    if final_update== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The book is not found')
    update_one.update(book.dict(),synchronize_session = False)
    db.commit()
    return {f'the book with the id of {id} successfully updated, Thanks'}