"""Adding publication year to books table

Revision ID: d88a20bc318e
Revises: df34d3f0af24
Create Date: 2019-10-22 19:28:10.294682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d88a20bc318e"
down_revision = "df34d3f0af24"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("books", sa.Column("publication_year", sa.Integer(), nullable=False))


def downgrade():
    op.drop_column("books", "publication_year")
