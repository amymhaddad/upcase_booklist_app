from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.orm import relationship
from upcase_booklist_app.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    category_name = Column(String, nullable=True)

    # books = relationship("Books", back_populates="categories")


