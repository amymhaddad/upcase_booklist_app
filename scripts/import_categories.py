

from upcase_booklist_app.database import db_session
from upcase_booklist_app.models.category import Category
import random


programming_categories = ["Beginner", "Intermediate", "Advanced"]
session = db_session()

categories = []

for _ in range(100):
    category = Category(
        category_name = random.choice(programming_categories)
    )

    categories.append(category)

session.add_all(category)
session.commit()
