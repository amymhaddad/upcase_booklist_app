"""Add relationship between categories and books

Revision ID: 7de08afa7fcc
Revises: 6970c2f20ef4
Create Date: 2019-11-28 08:01:20.693374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7de08afa7fcc"
down_revision = "6970c2f20ef4"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("categories", sa.Column("book_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        op.f("fk_categories_book_id_books"), "categories", "books", ["book_id"], ["id"]
    )


def downgrade():
    op.drop_constraint(
        op.f("fk_categories_book_id_books"), "categories", type_="foreignkey"
    )
    op.drop_column("categories", "book_id")
