from .database import Base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50))
    squad = Column(String(100))

    user_answers = relationship("UserAnswer", back_populates="user")


class Round(Base):
    __tablename__ = "rounds"

    id = Column(Integer, primary_key=True)
    rounds = Column(String(50))
    date = Column(Date)


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    answer_text = Column(String(512))
    is_correct = Column(Boolean)

    question = relationship("Question", back_populates="answers")
    user_answers = relationship("UserAnswer", back_populates="answer")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    quiz_id = Column(Integer)
    question_text = Column(String(512))
    category = Column(String(512))
    difficulty = Column(String(512))

    answers = relationship("Answer", back_populates="question")
    user_answers = relationship("UserAnswer", back_populates="question")


class UserAnswer(Base):
    __tablename__ = "user_answers"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    answer_id = Column(Integer, ForeignKey("answers.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    quiz_id = Column(Integer)

    question = relationship("Question", back_populates="user_answers")
    answer = relationship("Answer", back_populates="user_answers")
    user = relationship("User", back_populates="user_answers")
