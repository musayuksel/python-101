from typing import Annotated
from fastapi import FastAPI, Body, Query
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    # name will be min 3 characters and max 50 characters
    name: str = Field(min_length=3, max_length=50)
    description: str | None = None
    price: float = Field(gt=-1,
                         description="The price must be greater than zero", default=0)
    # tax is optional, but if provided, it must be greater than zero, default to 0
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.post("/items/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
):
    results = {"item_id": item_id, "item": item,
               "user": user, "importance": importance}
    return results

# in this case, FastAPI will expect a body like:
# it will convert the data types, validate, document, etc.
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}


# NESTED MODELS
class Image(BaseModel):
    url: str
    name: str


class Item2(BaseModel):
    name: str
    image: list[Image] = []  # list of Image objects, default to empty list

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "image": [
                    {
                        "url": "http://example.com/baz.jpg",
                        "name": "The Foo live"
                    },
                    {
                        "url": "http://example.com/dave.jpg",
                        "name": "The Dave live"
                    }
                ]
            }
        }


@app.post("/images/{image_id}")
async def update_item(image_id: int, item2: Item2):
    results = {"image_id": image_id, "item2": item2}
    return results
