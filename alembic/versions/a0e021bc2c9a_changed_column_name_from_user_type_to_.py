"""Changed column name from user_type to user_level

Revision ID: a0e021bc2c9a
Revises: e16e230d5eb4
Create Date: 2019-11-09 08:27:29.693903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a0e021bc2c9a"
down_revision = "e16e230d5eb4"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("user_level", sa.String(), nullable=True))
    op.drop_column("users", "user_type")


def downgrade():
    op.add_column(
        "users",
        sa.Column("user_type", sa.VARCHAR(), autoincrement=False, nullable=True),
    )
    op.drop_column("users", "user_level")
