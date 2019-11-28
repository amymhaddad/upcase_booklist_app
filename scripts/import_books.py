from faker import Faker

fake = Faker()

from random import choice

import sys
from upcase_booklist_app.database import Base, db_session
from upcase_booklist_app.models.book import Book
from upcase_booklist_app.models.author import Author
from upcase_booklist_app.models.category import Category 
from sqlalchemy.sql.functions import random

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

    author = session.query(Author).order_by(random()).first()
    #add categories to import_books that way I get a category value
    category = session.query(Category).order_by(random()).first()

    book = Book(
        title=fake.company(),
        summary=fake.text(max_nb_chars=200, ext_word_list=None),
        image_url=choice(images),
        genre=choice(genres),
        publication_year=fake.year(),
        author=author,
        category=category,
    )
    books.append(book)

session.add_all(books)

session.commit()
