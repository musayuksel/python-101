
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item:
    # FastAPI will use this return type to:
    # # Validate the returned data
    # # Add a JSON Schema for the response, in the OpenAPI path operation
    # # It will limit and filter the output data to what is defined in the return type. This is particularly important for security
    return item


@app.get("/items/", response_model=list[Item])
async def read_items() -> any:
    # response_model will take priority and be used by FastAPI.
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]
