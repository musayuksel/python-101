# A request body is data sent by the client to your API. A response body is the data your API sends to the client.

from fastapi import FastAPI
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
