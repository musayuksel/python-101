# A request body is data sent by the client to your API. A response body is the data your API sends to the client.
from typing import Annotated
from fastapi import FastAPI, Query
from pydantic import BaseModel  # for request body


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
# post request body example
# {
#   "name": "Cup",
#   "description": "string",
#   "price": 10,
#   "tax": 0.1
# }
async def create_item(item: Item):
    # print("Item dict>>>>>>>>", type(item.dict()))
    # print("Item>>>>>>>>", type(item))
    item_dict = item.dict()
    if item.tax:
        # add the price_with_tax attribute to the item_dict if the tax is provided
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# Request body + path parameters + query parameters
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, optional: str | None = None):
    # unpack the item dict and add business logic
    result = {"item_id": item_id, **item.dict()}
    if optional:
        result.update({"optional": optional})
    return result


@app.get("/items/")
# Query parameters with validation
# Using Annotated is recommended instead of the default value in function parameters
async def read_items(
    # query parameters are optional and default to N/A
    # if you provide a value, it must be between 3 and 50 characters
    extra_info: Annotated[str, Query(
        min_length=3, max_length=50)] = "N/A"
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if extra_info:
        results.update({"extra_info": extra_info})
    return results
