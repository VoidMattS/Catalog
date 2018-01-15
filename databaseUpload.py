from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from finalproject_database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///catalog.db')
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

#create template user
User1 = User(name="jim jimmerson", email="me@me.com")
session.add(User1)
session.commit()

# category for football
category1 = Category(name="Football", user_id=1)

session.add(category1)
session.commit()

item2 = Item(name="ball", description="NFL regulation size; Durable and all weather resistent", user_id=1,
                     category=category1)

session.add(item2)
session.commit()


item1 = Item(name="Shoulder Pads", description="Adult size pads, protects against high impact collisions", user_id=1,
                     category=category1)

session.add(item1)
session.commit()

# Basketball Category
category2 = Category(name="BasketBall", user_id=1)

session.add(category2)
session.commit()


item1 = Item(name="Athletic Shoes", description="Durable all around athletic shoes", user_id=1,
                     category=category2)

session.add(item1)
session.commit()

item2 = Item(
    name="Ball", description="NBA regulation size; good grip, best used indoors", user_id=1, category=category2)

session.add(item2)
session.commit()


# BaseBall Category
category3 = Category(name="BaseBall", user_id=1)

session.add(category3)
session.commit()


item1 = Item(name="Bat", description="Sturdy all wood Louisville slugger", user_id=1,
                     category=category3)

session.add(item1)
session.commit()

item2 = Item(name="Helmet", description="Provides great protection from a stray pitch when at bat", user_id=1,
                     category=category3)

session.add(item2)
session.commit()

#category for hockey
category4 = Category(name="Hockey", user_id=1)

session.add(category4)
session.commit()


item1 = Item(name="Stick", description="Adult size stick; All wood contruction", user_id=1,
                     category=category4)

session.add(item1)
session.commit()

item2 = Item(name="Helmet", description="Protects from impact from players or pucks. Comes with optional face sheild", user_id=1,
                     category=category4)

session.add(item2)
session.commit()


print "Added Catalog categories and items!"
