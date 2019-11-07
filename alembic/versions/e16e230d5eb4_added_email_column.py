"""Added email column

Revision ID: e16e230d5eb4
Revises: 1f1957717c30
Create Date: 2019-11-09 08:17:07.589608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e16e230d5eb4"
down_revision = "1f1957717c30"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("email", sa.String(), nullable=True))


def downgrade():
    op.drop_column("users", "email")
