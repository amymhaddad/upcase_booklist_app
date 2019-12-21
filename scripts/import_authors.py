from faker import Faker

fake = Faker()
import random

from upcase_booklist_app.database import db_session
from upcase_booklist_app.models.author import Author

session = db_session()

authors = []

for _ in range(100):
    author = Author(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        biography=fake.paragraph(
            nb_sentences=3, variable_nb_sentences=True, ext_word_list=None
        ),
    )
    authors.append(author)

session.add_all(authors)

session.commit()
