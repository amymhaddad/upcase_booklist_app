from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from upcase_booklist_app.models.book import Book
from upcase_booklist_app.models.author import Author
from upcase_booklist_app.models.user import User

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost/curious_programmer",
    echo=True
)

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

