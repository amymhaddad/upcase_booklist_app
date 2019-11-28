from flask import Flask, render_template, request

from upcase_booklist_app.database import db_session
from upcase_booklist_app.models.book import Book
from upcase_booklist_app.models.author import Author
from upcase_booklist_app.models.user import User

from upcase_booklist_app.data.categories import categories

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    """Render the homepage"""
    return render_template("index.html")


@app.route("/books", methods=["GET", "POST"])
def book_list():
    """Show the list of books"""

    if request.method == "POST":
        user_genre = request.form["genre"]
        books = db_session.query(Book).filter(Book.genre == user_genre)

    elif request.method == "GET" and request.args:
        if request.args.get("page"):
            limit_books = request.args.get("page")
            books = db_session.query(Book).limit(10).offset(limit_books)

        elif request.args.get("sort"):
            sort_by = request.args.get("sort")
            books = db_session.query(Book).order_by(sort_by).all()
    else:
        books = db_session.query(Book).limit(10)

    return render_template("books.html", books=books)


@app.route("/books/<int:book_id>")
def book(book_id):
    """Show details for a specific book."""

    book = db_session.query(Book).filter(Book.id == book_id).one()

    return render_template("book.html", book=book)


@app.route("/authors", methods=["GET", "POST"])
def authors():
    """Show the list of authors and the books they've written"""

    if request.method == "POST":
        single_author = request.form["last_name"]
        authors = db_session.query(Author).filter(Author.last_name == single_author)

    elif request.method == "GET" and request.args:
        if request.args.get("page"):
            limit_authors = request.args.get("page")
            authors = db_session.query(Author).limit(10).offset(limit_authors)

        elif request.args.get("sort"):
            author_name = request.args.get("sort")
            authors = db_session.query(Author).order_by(author_name).all()

    else:
        authors = (
            db_session.query(Author).join(Book, Book.author_id == Author.id).limit(10)
        )

    return render_template("authors.html", authors=authors)


@app.route("/categories")
def categories():
    """Organize authors and their books into categories"""

    return render_template("categories.html", categories=categories)


@app.route("/categories/<int:category_id>")
def category(category_id):
    """Direct user to page about a specific category"""

    books_associated_with_selected_category = None
    category_title = None
    for category in categories:
        if category["category_id"] == category_id:
            books_associated_with_selected_category = category["books"]
            category_title = category["category"]

    return render_template(
        "category.html",
        category=books_associated_with_selected_category,
        category_title=category_title,
    )


@app.route("/authors/<int:author_id>")
def author(author_id):
    """Display a page about an author"""

    author = (
        db_session.query(Author)
        .join(Book, Book.author_id == Author.id)
        .filter(Author.id == author_id)
        .first()
    )

    return render_template("author.html", author=author)


@app.route("/users", methods=["GET", "POST"])
def users():
    """Show all of the users and basic user details"""

    if request.method == "POST":
        if request.form.get("user_level"):
            programming_level = request.form["user_level"]
            users = db_session.query(User).filter(User.user_level == programming_level)

        elif request.form.get("last_name"):
            user_last_name = request.form["last_name"]
            users = db_session.query(User).filter(User.last_name == user_last_name)

    elif request.method == "GET" and request.args:
        if request.args.get("sort"):
            sort_by = request.args.get("sort")
            users = db_session.query(User).order_by(sort_by)

        elif request.args.get("page"):
            limit_users = request.args.get("page")
            users = db_session.query(User).limit(10).offset(limit_users)

    else:
        users = db_session.query(User).limit(10)

    return render_template("users.html", users=users)


@app.route("/users/<int:user_id>")
def user(user_id):
    """Display user details"""

    user = db_session.query(User).filter(User.id == user_id).one()

    return render_template("user.html", user=user)


if __name__ == "__main__":
    app.run()
