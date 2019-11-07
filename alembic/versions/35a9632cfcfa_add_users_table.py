"""Add users table

Revision ID: 35a9632cfcfa
Revises: 9e475da39630
Create Date: 2019-11-07 07:34:55.790734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "35a9632cfcfa"
down_revision = "9e475da39630"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("account_start_date", sa.DateTime(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("user_type", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("users")
