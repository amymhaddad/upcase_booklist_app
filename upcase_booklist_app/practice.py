from flask import Flask, render_template, url_for
app = Flask(__name__)


single_book_details = {'title': 'Python Crash Course', 'author': "Eric Matthes", 'summary': 'A hands-on introduction to programming with Python.', 'date': '2016', 'image': 'img/python_crash_course.jpeg'}

for category, details in  single_book_details.items():
   
    if category=='title':
        print(single_book_details[category])




# <li class="booklist"><a href="{{ url_for('single_book', title=details['title']) }}">{{ details['title'] }}</a></li>
# <img class="images" src="{{ details['image'] }}" alt="{{ details['title'] }}"> 






# ex:


# <a href="https://www.mozilla.org/en-US/">
#     <img src="mozilla-image.png" alt="mozilla logo that links to the mozilla homepage">
#   </a>

