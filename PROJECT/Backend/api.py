from fastapi import FastAPI
# from pydantic import BaseModel  # for request body

from fastapi.middleware.cors import CORSMiddleware
from questions import current_quiz

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


@app.get("/api/current_quiz")
async def read_root():
    return {"current_quiz": current_quiz}
