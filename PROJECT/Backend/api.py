from fastapi import FastAPI
# from pydantic import BaseModel  # for request body

from fastapi.middleware.cors import CORSMiddleware
from questions import questions

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/questions")
async def read_root():
    return {"questions": questions}
