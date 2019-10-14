"""Get books table added to database

Revision ID: b78cdaa6e6ec
Revises: 7b49481bf438
Create Date: 2019-10-10 07:50:37.802228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b78cdaa6e6ec"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "books",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("author_id", sa.Integer(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("summary", sa.String(), nullable=False),
        sa.Column("image_url", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("books")
