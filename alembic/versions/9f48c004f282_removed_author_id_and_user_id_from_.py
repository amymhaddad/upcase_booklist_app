"""Removed author_id and user_id from Books table

Revision ID: 9f48c004f282
Revises: c7a2d0f9b089
Create Date: 2019-10-12 13:19:35.399249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9f48c004f282"
down_revision = "b78cdaa6e6ec"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("books", "user_id")
    op.drop_column("books", "author_id")


def downgrade():
    op.add_column(
        "books",
        sa.Column("author_id", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "books", sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=True)
    )
