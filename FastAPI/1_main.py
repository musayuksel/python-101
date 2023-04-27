# uvicorn main:app --reload  # --reload: auto reload when code changes
# from typing import Union
# FastAPI is a Python class that provides all the functionality for your API.
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel  # for request body

# The app variable will be an "instance" of the class FastAPI.
# This will be the main point of interaction to create all your API.
# This app is the same one referred by uvicorn in the command:uvicorn main:app --reload
app = FastAPI()

# Request body


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


# Empty list to store items
items: list[Item] = []


@app.get("/")  # in OpenAPI, each of the HTTP methods is called an "operation".
# Define a path operation decorator
async def read_root():
    return {"message": "Hello World!"}

# SIMILAR TO NODEJS ROUTES, THE ORDER MATTERS FOR THE PATHS


@app.get("/items/")
async def read_items():
    # print(items[0].name) # It will suggest the name attribute thanks to type hinting
    return {"items": items}


# http://127.0.0.1:8000/items/5?query=Musa&isGift=false  # # isGift is optional and might be False | false | 0 | 1 | True | true |on | off| yes | no
# # query is optional
@app.get("/items/{item_id}")
# The value of the path parameter item_id will be passed to your function as the argument item_id
# async def read_item(item_id: int, query: Union[str, None] = None):
async def read_item(item_id: int, query: str | None = None, isGift: bool = False):
    # with that type declaration, FastAPI gives you automatic request "parsing".
    return {"item_id": item_id, "query": query, "isGift": isGift}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.post("/items/")
async def create_item(item: Item):
    items.append(item)
    return {"message": "Item created"}


# define a default endpoint to handle all other requests
@app.get("/{path:path}")
async def catch_all(path: str):
    raise HTTPException(
        status_code=404,
        detail={
            "message": "Endpoint not found. Please check your link."
        })
