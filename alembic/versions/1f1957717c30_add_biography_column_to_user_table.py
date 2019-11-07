"""Add biography column to user table

Revision ID: 1f1957717c30
Revises: 35a9632cfcfa
Create Date: 2019-11-07 07:52:48.056937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1f1957717c30"
down_revision = "35a9632cfcfa"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("biography", sa.String(), nullable=True))


def downgrade():
    op.drop_column("users", "biography")
