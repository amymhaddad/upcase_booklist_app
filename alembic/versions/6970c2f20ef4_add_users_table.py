"""Add users table

Revision ID: 6970c2f20ef4
Revises: 4f179c7b94cb
Create Date: 2019-11-28 07:47:46.359169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6970c2f20ef4"
down_revision = "4f179c7b94cb"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "categories",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("category_name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_categories")),
    )


def downgrade():
    op.drop_table("categories")
