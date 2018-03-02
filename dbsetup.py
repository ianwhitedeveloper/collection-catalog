import sys

# come in handy when writing mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# use in configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# to create foreign key relationships
from sqlalchemy.orm import relationship

# use in config code at end of file
from sqlalchemy import create_engine

# will let sql alchemy know that our classes are special sql classes that
# correspond to tables in our db
Base = declarative_base()

class Collection(Base):
    __tablename__ = 'collection'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class CollectionItem(Base):
    __tablename__ = 'items'     #previously collection_item

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    category = Column(String(250))
    collection_id = Column(Integer, ForeignKey('collection.id'))
    collection = relationship(Collection)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'category': self.category
        }


#### add to end of file ###

# create instance of create_engine class, and point to db we will use
engine = create_engine('sqlite:///collectioncatalog.db')

 # adds classes we will create as new tables in db
Base.metadata.create_all(engine)
