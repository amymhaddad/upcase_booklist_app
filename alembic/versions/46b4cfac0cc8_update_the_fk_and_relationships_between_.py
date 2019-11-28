"""Update the FK and relationships between categories and books - version 2

Revision ID: 46b4cfac0cc8
Revises: 7de08afa7fcc
Create Date: 2019-12-01 11:44:42.507675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "46b4cfac0cc8"
down_revision = "7de08afa7fcc"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("books", sa.Column("category_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        op.f("fk_books_category_id_categories"),
        "books",
        "categories",
        ["category_id"],
        ["id"],
    )
    op.drop_constraint("fk_categories_book_id_books", "categories", type_="foreignkey")
    op.drop_column("categories", "book_id")


def downgrade():
    op.add_column(
        "categories",
        sa.Column("book_id", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.create_foreign_key(
        "fk_categories_book_id_books", "categories", "books", ["book_id"], ["id"]
    )
    op.drop_constraint(
        op.f("fk_books_category_id_categories"), "books", type_="foreignkey"
    )
    op.drop_column("books", "category_id")
