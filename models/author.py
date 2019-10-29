from sqlalchemy import Column, Integer, String 
from upcase_booklist_app.database import Base

class Author(Base):

    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    biography = Column(String(), nullable=True)

    @property
    def display_name(self):
        return f"{self.first_name} {self.last_name}"