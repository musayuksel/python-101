# To avoid confusion between the SQLAlchemy models and the Pydantic models, we will have the file models.py with the SQLAlchemy models, and the file schemas.py with the Pydantic models.

# Create initial Pydantic models / schemas
from pydantic import BaseModel


class ItemBase(BaseModel):
    # Pydantic models will be used to validate the data sent to and from the API endpoints.
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass
# The ItemCreate model will be used when creating an item. It will have the same attributes as the ItemBase model, but the description attribute will be optional.


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
        # The orm_mode attribute will tell the Pydantic model to read the data even if it is not a dict, but an ORM model (or any other arbitrary object with attributes).
        # This way, instead of only trying to get the id value from a dict, as in:
        # item_data["id"]
        # It will also try to get the id value from an ORM model, as in:
        # item_model.id


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True


# SQLAlchemy style and Pydantic style
#  SQLAlchemy style: name = Column(String)
# Pydantic style: name: str
