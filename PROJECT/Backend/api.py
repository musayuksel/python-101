from fastapi import FastAPI
# from pydantic import BaseModel  # for request body

from fastapi.middleware.cors import CORSMiddleware
from questions import current_quiz
from user_scores import user_score_list
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


@app.get("/api/user_scores")
async def user_scores():
    sorted_user_scores = sorted(
        user_score_list, key=lambda user_score:  user_score['score'], reverse=True)
    return {"user_scores": sorted_user_scores}
