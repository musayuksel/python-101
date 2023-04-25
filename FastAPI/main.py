# uvicorn main:app --reload  # --reload: auto reload when code changes
from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, query: Union[str, None] = None):
    return {"item_id": item_id, "query": query}
