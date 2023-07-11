from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text, func
from sqlalchemy.orm import relationship, column_property
from sqlalchemy.sql import select


class Book(Base):
    __tablename__='books'
    id=Column(Integer,primary_key=True, autoincrement=True)
    author_id= Column(Integer)
    title=Column(String(255),nullable=False)
    pages=Column(Integer)

    def __repr__(self):
        return f"<Book title={self.title}>"

class Author(Base):
    __tablename__='authors'
    id=Column(Integer,primary_key=True, autoincrement=True)
    name=Column(String(255),nullable=False)
    
    def __repr__(self):
        return f"<Author name={self.name}>"

