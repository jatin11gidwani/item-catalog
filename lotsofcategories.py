from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CatalogItem, User

engine = create_engine('sqlite:///categorywithusers.db')
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


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')  # noqa
session.add(User1)
session.commit()

# Category for Books
category1 = Category(user_id=1, name="Books")

session.add(category1)
session.commit()

catalogItem1 = CatalogItem(user_id=1, name="Rich Dad, Poor Dad",
                           description="Self-help book",
                           category=category1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Sherlock Holmes",
                           description="Thriller",
                           category=category1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Steve Jobs",
                           description="Biography",
                           category=category1)

session.add(catalogItem3)
session.commit()


# Category for Games
category2 = Category(user_id=1, name="Games")

session.add(category2)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Dota 2", description="Moba",
                           category=category2)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="CS:GO", description="FPS",
                           category=category2)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Pinball", description="Timepass",
                           category=category2)

session.add(catalogItem3)
session.commit()

print "added categories!"
