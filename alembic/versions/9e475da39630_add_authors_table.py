"""Add authors table

Revision ID: 9e475da39630
Revises: 7b206ee27574
Create Date: 2019-10-29 18:16:48.923017

"""
from alembic import op
import sqlalchemy as sa

revision = "9e475da39630"
down_revision = "7b206ee27574"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "authors",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("biography", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("authors")
