from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship
from upcase_booklist_app.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    category_name = Column(String, nullable=True)

    book_id = Column(Integer, ForeignKey("books.id"))
    books = relationship("Book", back_populates="categories")
