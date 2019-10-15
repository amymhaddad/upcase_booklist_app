from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship
from upcase_booklist_app.database import Base


class Book(Base):

    __tablename__ = "books"

    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    summary = Column(String(), nullable=False)
    image_url = Column(String(), nullable=False)
