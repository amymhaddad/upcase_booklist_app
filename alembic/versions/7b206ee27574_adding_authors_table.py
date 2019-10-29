"""Change nullables on books tables

Revision ID: 7b206ee27574
Revises: d88a20bc318e
Create Date: 2019-10-29 06:59:29.023758

"""
from alembic import op
import sqlalchemy as sa


revision = "7b206ee27574"
down_revision = "d88a20bc318e"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("books", "image_url", existing_type=sa.VARCHAR(), nullable=True)
    op.alter_column("books", "summary", existing_type=sa.VARCHAR(), nullable=True)


def downgrade():
    op.alter_column("books", "summary", existing_type=sa.VARCHAR(), nullable=False)
    op.alter_column("books", "image_url", existing_type=sa.VARCHAR(), nullable=False)
