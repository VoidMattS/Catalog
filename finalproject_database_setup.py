import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#Sets up the User Cass  
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

#sets up the category class
class Category(Base):
    __tablename__= 'category'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    item = relationship('Item', cascade='all, delete-orphan')


#sets up the item class
class Item(Base):
    __tablename__='item'

    name = Column( String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)



    @property
    def serialize(self):
        #returns object data 
        return {
            'name': self.name,
            'description':self.description,
            'id':self.id,
     }


#makes the catalog.db file using above classes
engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)
