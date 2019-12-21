from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship
from upcase_booklist_app.database import Base


class Book(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(), nullable=False)
    summary = Column(String(), nullable=True)
    image_url = Column(String(), nullable=True)
    genre = Column(String(), nullable=False)
    publication_year = Column(Integer, nullable=False)

    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="books")
