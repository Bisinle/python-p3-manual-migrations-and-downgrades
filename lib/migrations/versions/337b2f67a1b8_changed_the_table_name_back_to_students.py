"""changed the table name back to students

Revision ID: 337b2f67a1b8
Revises: ce6d7a0377e5
Create Date: 2023-08-31 00:32:52.370555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "337b2f67a1b8"
down_revision = "ce6d7a0377e5"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table("mirio_students", "students")


def downgrade() -> None:
    op.rename_table("students", "mirio_students")
