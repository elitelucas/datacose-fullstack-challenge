from fastapi import FastAPI,status,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models

app=FastAPI()

# Add CORS middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Book(BaseModel): #serializer
    id:int
    author_id:int  
    title:str  

    class Config:
        orm_mode=True    

class Author(BaseModel): #serializer
    id:int
    name:str 

    class Config:
        orm_mode=True        



db=SessionLocal()

# Authors
@app.get('/authors',response_model=List[Author],status_code=200)
def get_all_items():
    items=db.query(models.Author).all()

    return items

@app.post('/authors',response_model=Author,
        status_code=status.HTTP_201_CREATED)
def create_an_author(item:Author):
    db_item=db.query(models.Item).filter(models.Author.name==item.name).first()

    if db_item is not None:
        raise HTTPException(status_code=400,detail="Author already exists")

    new_item=models.Author(
        name=item.name
    )

    db.add(new_item)
    db.commit()

    return new_item

@app.post('/authors/del/{item_id}')
def delete_item(item_id:int):
    item_to_delete=db.query(models.Author).filter(models.Author.id==item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(item_to_delete)
    db.commit()

    return item_to_delete
# Books
@app.get('/books',response_model=List[Book],status_code=200)
def get_all_items():
    items=db.query(models.Book).all()

    return items

@app.post('/books',response_model=Book,
        status_code=status.HTTP_201_CREATED)
def create_an_book(item:Book):
    # db_item=db.query(models.Book).filter(models.Book.title==item.title).first()

    # if db_item is not None:
    #     raise HTTPException(status_code=400,detail="Book already exists")

    new_item=models.Book(
        author_id=item.author_id,
        title=item.title
    )

    db.add(new_item)
    db.commit()

    return new_item

@app.post('/books/del/{item_id}')
def delete_item(item_id:int):
    item_to_delete=db.query(models.Book).filter(models.Book.id==item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(item_to_delete)
    db.commit()

    return item_to_delete