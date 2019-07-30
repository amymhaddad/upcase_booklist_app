from flask import Flask, render_template, url_for
from upcase_booklist_app.data.books import books

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    """Render the homepage"""
    return render_template("index.html")


@app.route("/books")
def book_list():
    """Show the list of books"""
    return render_template("books.html", books=books)


@app.route("/books/<int:book_id>")
def book(book_id):
    """Show details for a specific book."""
    return render_template("book.html", book= books[book_id])


@app.route("/authors")
def authors():
    """Show the list of authors and the books they've written"""
    return render_template("authors.html", books=books)


if __name__ == "__main__":
    app.run()
