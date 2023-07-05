from typing import List
from pydantic import BaseModel
from datetime import date


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    squad: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class RoundBase(BaseModel):
    rounds: str
    date: date


class RoundCreate(RoundBase):
    pass


class Round(RoundBase):
    id: int

    class Config:
        orm_mode = True


class AnswerBase(BaseModel):
    question_id: int
    answer_text: str
    is_correct: bool


class AnswerCreate(AnswerBase):
    pass


class Answer(AnswerBase):
    id: int

    class Config:
        orm_mode = True


class QuestionBase(BaseModel):
    quiz_id: int
    question_text: str
    category: str
    difficulty: str


class QuestionCreate(QuestionBase):
    pass


class Question(QuestionBase):
    id: int
    answers: List[Answer] = []

    class Config:
        orm_mode = True


class UserAnswerBase(BaseModel):
    question_id: int
    answer_id: int
    user_id: int
    quiz_id: int


class UserAnswerCreate(UserAnswerBase):
    pass


class UserAnswer(UserAnswerBase):
    id: int

    class Config:
        orm_mode = True
