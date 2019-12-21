"""Create relationship between author and book tables

Revision ID: 4f179c7b94cb
Revises: a0e021bc2c9a
Create Date: 2019-11-21 20:11:11.224837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4f179c7b94cb"
down_revision = "a0e021bc2c9a"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("books", sa.Column("author_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        op.f("fk_books_author_id_authors"), "books", "authors", ["author_id"], ["id"]
    )


def downgrade():
    op.drop_constraint(op.f("fk_books_author_id_authors"), "books", type_="foreignkey")
    op.drop_column("books", "author_id")
