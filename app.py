from flask import Flask, render_template, request, abort

from upcase_booklist_app.database import db_session
from upcase_booklist_app.models.book import Book
from upcase_booklist_app.models.author import Author
from upcase_booklist_app.models.user import User
from upcase_booklist_app.models.category import Category

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
        last_name = request.form["last_name"]
        authors = (
            db_session.query(Author)
            .join(Book, Author.id == Book.author_id)
            .filter(Author.last_name == last_name)
        )
        if last_name not in authors:
            abort(404)

    elif request.method == "GET" and request.args:
        if request.args.get("author_firstname"):
            first_name = request.args.get("first_name")
            authors = (
                db_session.query(Author)
                .join(Book, Author.id == Book.author_id)
                .order_by(Author.first_name)
            )
        else:
            last_name = request.args.get("last_name")
            authors = (
                db_session.query(Author)
                .join(Book, Author.id == Book.author_id)
                .order_by(Author.last_name)
            )

    else:
        authors = (
            db_session.query(Author).join(Book, Book.author_id == Author.id).limit(10)
        )

    return render_template("authors.html", authors=authors)


@app.route("/categories", methods=["GET", "POST"])
def categories():
    """Organize books into categories"""

    if request.method == "POST":
        category = request.form["category"]
        categories = (
            db_session.query(Book)
            .join(Category, Book.category_id == Category.id)
            .filter(Category.category_name == category)
            .order_by(Book.title)
            .all()
        )
    elif request.method == "GET" and request.args:
        if request.args.get("category_level"):
            category = request.args.get("category_level")
            categories = (
                db_session.query(Book)
                .join(Category, Book.category_id == Category.id)
                .filter(Category.category_name == category)
                .order_by(Book.title)
                .all()
            )

        elif request.args.get("sort"):
            level = request.args.get("sort")
            categories = (
                db_session.query(Book)
                .join(Category, Book.category_id == Category.id)
                .order_by(Book.title)
                .all()
            )

    else:
        categories = (
            db_session.query(Book)
            .join(Category, Book.category_id == Category.id)
            .order_by(Category.category_name)
            .all()
        )

    return render_template("categories.html", categories=categories)


@app.route("/categories/<int:category_id>")
def category(category_id):
    """Direct user to page about a specific category"""

    category = (
        db_session.query(Category)
        .join(Book, Category.id == Book.category_id)
        .filter(Category.id == category_id)
        .first()
    )

    return render_template("category.html", category=category)


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
