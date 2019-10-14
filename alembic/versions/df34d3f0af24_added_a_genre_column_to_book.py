"""Added a 'genre' column to Book

Revision ID: df34d3f0af24
Revises: 9f48c004f282
Create Date: 2019-10-18 06:58:37.574717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "df34d3f0af24"
down_revision = "9f48c004f282"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("books", sa.Column("genre", sa.String(), nullable=False))


def downgrade():
    op.drop_column("books", "genre")
