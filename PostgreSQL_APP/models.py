# Create SQLAlchemy models from the Base class
# This file will contain the SQLAlchemy models (or classes) that we will use to interact with the database.

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
# The relationship function is not actually a column, but a relationship between two columns. It will allow us to create a foreign key relationship between the items table and the users table.

# Import the Base class from the database.py file
from .database import Base


class User(Base):  # Create classes that inherit from it.
    # These classes will be the SQLAlchemy models.
    # Each class will be a table in the database.
    # Each attribute of the class will be a column in the database.
    # Each instance of the class will be a row in the table.

    __tablename__ = "users"
    # The __tablename__ attribute is optional but recommended. It allows us to define the table name ourselves. In this case, we define the table name as users.

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
    # When you access my_user.items, SQLAlchemy will actually go and fetch the items from the database in the items table and populate them here.


class Item(Base):
    # Each class will be a table in the database.
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
    # And when accessing the attribute "owner" in an Item, it will contain a "User" SQLAlchemy model from the users table. It will use the owner_id attribute/column with its foreign key to know which record to get from the users table.
    # The back_populates argument will make the relationship bidirectional. It means that if you access my_item.owner, you will get the user that owns that item.
