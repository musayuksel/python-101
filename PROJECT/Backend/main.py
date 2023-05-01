# To deploy the backend server to GOOGLE CLOUD use the following link:
# https://tutlinks.com/deploy-fastapi-app-on-google-cloud-platform/


from fastapi import FastAPI, status
from pydantic import BaseModel  # for request body

from fastapi.middleware.cors import CORSMiddleware
from questions import current_quiz
from user_scores import user_score_list


class UserScores(BaseModel):
    name: str
    score: int


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
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


@app.post("/api/user_scores", status_code=status.HTTP_201_CREATED)
async def user_scores(user_scores: UserScores):
    user_score = user_scores.dict()
    next_id = len(user_score_list) + 1
    user_score.update({"id": next_id})
    user_score_list.append(user_scores.dict())
    return {"message": "User score created successfully"}
