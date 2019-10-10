from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Book(Base):

    __tablename__ = "books"

    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    summary = Column(String(), nullable=False)
    image_url = Column(String(), nullable=False)
