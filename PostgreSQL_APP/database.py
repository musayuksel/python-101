from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

# Create the SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# Create the SQLAlchemy session factory
# Each instance of the SessionLocal class will be a database session. The class itself is not a database session yet.
# Once we create an instance of the SessionLocal class, we will be able to use it to perform CRUD operations on the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base class for our database models
# Any class that we define that inherits from this class will be a SQLAlchemy model.
# Later we will inherit from this class to create each of the database models or classes (the ORM models)
Base = declarative_base()
