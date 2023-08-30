"""name changed to moringa

Revision ID: da4b5df0bccf
Revises: 337b2f67a1b8
Create Date: 2023-08-31 00:45:53.207216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "da4b5df0bccf"
down_revision = "337b2f67a1b8"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table("students", "moringa")


def downgrade() -> None:
    op.rename_table("moringa", "students")
