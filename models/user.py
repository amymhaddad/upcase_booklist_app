from sqlalchemy import Column, Integer, String, DateTime
from upcase_booklist_app.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    account_start_date = Column(DateTime(), nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    user_level = Column(String, nullable=True)
    biography = Column(String, nullable=True)
    email = Column(String, nullable=True)

    @property
    def display_name(self):
        return f"{self.first_name} {self.last_name}"
