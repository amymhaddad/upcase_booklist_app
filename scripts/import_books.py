from faker import Faker

fake = Faker()
import random

import sys
from upcase_booklist_app.database import Base, db_session
from upcase_booklist_app.models.book import Book

session = db_session()


genres = ["Beginner", "Intermediate", "Advanced"]

images = [
    "/static/img/python_crash_course.jpeg",
    "/static/img/grokking_algorithms.jpeg",
    "/static/img/the_quick_python_book.jpeg",
    "/static/img/irresistible_APIs.jpeg",
    "/static/img/intro_to_computer_science.jpg",
]


books = []

for _ in range(100):
    book = Book(
        title=fake.company(),
        summary=fake.text(max_nb_chars=200, ext_word_list=None),
        image_url=random.choice(images),
        genre=random.choice(genres),
        publication_year=fake.year(),
    )
    books.append(book)

session.add_all(books)

session.commit()
