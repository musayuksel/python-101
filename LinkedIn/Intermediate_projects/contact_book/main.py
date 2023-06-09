from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

# Create all the tables in the database.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create a user
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if the user already exists
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # If the user does not exist, create it
    return crud.create_user(db=db, user=user)


# Get all users
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Get all users
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


# Get a user by id
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    # Get the user by id
    db_user = crud.get_user(db, user_id=user_id)
    # If the user does not exist, raise an error
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    # If the user exists, return it
    return db_user


# Create a contact for a user
@app.post("/users/{user_id}/contacts/", response_model=schemas.Contact)
def create_contact_for_user(
    user_id: int, contact: schemas.ContactCreate, db: Session = Depends(get_db)
):
    # Check if the user exists
    db_user = crud.get_user(db, user_id=user_id)
    # If the user does not exist, raise an error
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    # If the user exists, create the contact
    return crud.create_user_contact(db=db, contact=contact, user_id=user_id)


# Get all contacts
@app.get("/contacts/", response_model=list[schemas.Contact])
def read_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Get all contacts
    contacts = crud.get_contacts(db, skip=skip, limit=limit)
    return contacts
