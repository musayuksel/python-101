# uvicorn main:app --reload  # --reload: auto reload when code changes
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel  # for request body

app = FastAPI()

# Request body


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
async def read_root():
    return {"message": "Hello World!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, query: Union[str, None] = None):
    return {"item_id": item_id, "query": query}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
