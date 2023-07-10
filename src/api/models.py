from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text, func
from sqlalchemy.orm import relationship, column_property
from sqlalchemy.sql import select


class Item(Base):
    __tablename__='items'
    id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False,unique=True)
    description=Column(Text)
    price=Column(Integer,nullable=False)
    on_offer=Column(Boolean,default=False)


    def __repr__(self):
        return f"<Item name={self.name} price={self.price}>"


class Book(Base):
    __tablename__='books'
    id=Column(Integer,primary_key=True, autoincrement=True)
    author_id= Column(Integer)
    title=Column(String(255),nullable=False)

    def __repr__(self):
        return f"<Book name={self.name}>"

class Author(Base):
    __tablename__='authors'
    id=Column(Integer,primary_key=True, autoincrement=True)
    name=Column(String(255),nullable=False)
    
    def __repr__(self):
        return f"<Author name={self.name}>"

