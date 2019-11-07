from faker import Faker
from upcase_booklist_app.database import db_session
from upcase_booklist_app.models.user import User
import random

fake = Faker()
session = db_session()

user_levels = ["Beginner", "Intermediate", "Advanced"]

users = []
for _ in range(100):
    user = User(
        account_start_date=fake.date(pattern="%Y-%m-%d", end_datetime=None),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        user_level=random.choice(user_levels),
        biography=fake.paragraph(
            nb_sentences=3, variable_nb_sentences=True, ext_word_list=None
        ),
        email=fake.ascii_email(),
    )
    users.append(user)

session.add_all(users)

session.commit()
