from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)



BOOKS = {
    "book1" : {'title': 'Python Crash Course', 'author': "Eric Matthes", 'summary': 'A hands-on introduction to programming with Python.', 'date': '2016', 'image': '/static/img/python_crash_course.jpeg'},
    "book2" : {'title': 'Grokking Algorithms', 'author': 'Aditya Bhargava', 'summary': 'Learn how to apply common algorithms to practical programming problesm.', 'date': '2016', 'image': '/static/img/grokking_algorithms.jpeg'},
    "book3" : {'title': 'The Quick Python Book', 'author': 'Naomi Ceder', 'summary': 'A comprehensive guide to Python.', 'date': '2018', 'image': '/static/img/the_quick_python_book.jpeg'},
    "book4" : {'title': 'Irresistible APIs', 'author': "Kristen Hunter", 'summary': 'Learn the process to create APIs', 'date': '2017', 'image': '/static/img/irresistible_APIs.jpeg'},
    "book5" : {'title': 'Introduction to Computer Science and Programming Using Python', 'author': "John Guttag", 'summary': 'An introduction to programming and computational problem solving, using Python.', 'date': '2016', 'image': '/static/img/intro_to_computer_science.jpg'},
}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/books')
def book_list():
    return render_template('book_list.html', BOOKS=BOOKS)


@app.route('/books/<title>')
def single_book(title):
    return render_template('single_book.html', single_book_details=BOOKS[title])




if __name__=="__main__":
    app.run()

#Update single_book view funciton to return the necsessary details (ie, the dictionary for the specific book)
#Update single_book.html
#Add book titles and information

#Add images to the book list page AND for single book


#NOTES:
# the url_for() function. It accepts the name of the function as its first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule
#<p class="nav-item"><a href="{{ url_for('book_list') }}">Books</a></p>