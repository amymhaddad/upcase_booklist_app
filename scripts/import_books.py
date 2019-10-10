import sys
from database import Base, db_session
from models.book import Book

session = db_session()


session.add_all(
    [
        Book(
            title="Python Crash Course",
            summary="A hands-on introduction to programming with Python.",
            image_url="/static/img/python_crash_course.jpeg",
        ),
        Book(
            title="Grokking Algorithms",
            summary="Learn how to apply common algorithms to practical programming problems.",
            image_url="/static/img/grokking_algorithms.jpeg",
        ),
        Book(
            title="The Quick Python Book",
            summary="A comprehensive guide to Python.",
            image_url="/static/img/the_quick_python_book.jpeg",
        ),
        Book(
            title="Irresistible APIs",
            summary="Learn the process to create APIs",
            image_url="/static/img/irresistible_APIs.jpeg",
        ),
        Book(
            title="Introduction to Computer Science and Programming Using Python",
            summary="An introduction to programming and computational problem solving, using Python.",
            image_url="/static/img/intro_to_computer_science.jpg",
        ),
    ]
)

session.commit()
