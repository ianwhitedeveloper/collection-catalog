from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dbsetup import Base, Collection, CollectionItem

engine = create_engine('sqlite:///collectioncatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Items for Yoga Collection
yoga = Collection(name="Yoga")

session.add(yoga)
session.commit()

collectionItem1 = CollectionItem(name="Long Sleeve", description="#",
                     price="$39.99", category="clothing", collection=yoga)

session.add(collectionItem1)
session.commit()


collectionItem2 = CollectionItem(name="Flow Tank", description="#",
                     price="$29.99", category="clothing", collection=yoga)

session.add(collectionItem2)
session.commit()

collectionItem3 = CollectionItem(name="High Rise Tight", description="#",
                     price="$59.99", category="clothing", collection=yoga)

session.add(collectionItem3)
session.commit()

collectionItem4 = CollectionItem(name="Yoga Mat", description="#",
                     price="$19.99", category="accessories", collection=yoga)

session.add(collectionItem4)
session.commit()

collectionItem5 = CollectionItem(name="Headband", description="#",
                     price="$9.99", category="accessories", collection=yoga)

session.add(collectionItem5)
session.commit()



# Items for Run Category

run = Collection(name="Run")

session.add(run)
session.commit()

collectionItem1 = CollectionItem(name="Reflective Pullover", description="#",
                     price="$59.99", category="clothing", collection=run)

session.add(collectionItem1)
session.commit()

collectionItem2 = CollectionItem(name="Run Tank", description="#",
                     price="$29.99", category="clothing", collection=run)

session.add(collectionItem2)
session.commit()

collectionItem3 = CollectionItem(name="Reflective Tight", description="#",
                     price="$59.99", category="clothing", collection=run)

session.add(collectionItem3)
session.commit()

collectionItem4 = CollectionItem(name="Run Shorts", description="#",
                     price="$39.99", category="clothing", collection=run)

session.add(collectionItem4)
session.commit()

collectionItem5 = CollectionItem(name="Headband", description="#",
                     price="$9.99", category="accessories", collection=run)

session.add(collectionItem5)
session.commit()

collectionItem6 = CollectionItem(name="Socks", description="#",
                     price="$14.99", category="accessories", collection=run)

session.add(collectionItem6)
session.commit()



# Items for Train Category
train = Collection(name="Train")

session.add(train)
session.commit()

collectionItem1 = CollectionItem(name="Short Sleeve", description="#",
                     price="$29.99", category="clothing", collection=train)

session.add(collectionItem1)
session.commit()


collectionItem2 = CollectionItem(name="Crop Tank", description="#",
                     price="$29.99", category="clothing", collection=train)

session.add(collectionItem2)
session.commit()

collectionItem3 = CollectionItem(name="Train Tight", description="#",
                     price="$59.99", category="clothing", collection=train)

session.add(collectionItem3)
session.commit()

collectionItem4 = CollectionItem(name="Headband", description="#",
                     price="$9.99", category="accessories", collection=train)

session.add(collectionItem4)
session.commit()

collectionItem5 = CollectionItem(name="Weight Set", description="#",
                     price="$99.99", category="accessories", collection=train)

session.add(collectionItem5)
session.commit()


print "added collection items!"
