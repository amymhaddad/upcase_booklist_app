from flask import Flask, render_template, url_for
from upcase_booklist_app.data.books import books
from upcase_booklist_app.data.categories import categories
from upcase_booklist_app.data.author import authors as authors_data


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

    return render_template("book.html", book=books[book_id])


@app.route("/authors")
def authors():
    """Show the list of authors and the books they've written"""
    return render_template("authors.html", authors=authors_data)


@app.route("/lists")
def lists():
    """Organize authors and their books into categories"""

    return render_template("lists.html", categories=categories)


@app.route("/lists/<int:category_id>")
def category(category_id):
    """Direct user to page about a specific category"""

    books_asscoiated_with_selected_category = None
    category_title = None
    for category in categories:
        if category["category_id"] == category_id:
            books_asscoiated_with_selected_category = category["books"]
            category_title = category["category"]

    return render_template(
        "category.html", category=selected_category, category_title=category_title
    )


@app.route("/authors/<int:author_id>")
def author(author_id):
    """Display a page about an author"""

    author_object = None
    for author in authors_data:
        if author["author_id"] == author_id:
            author_object = author

    return render_template("author.html", author_object=author_object)


if __name__ == "__main__":
    app.run()
