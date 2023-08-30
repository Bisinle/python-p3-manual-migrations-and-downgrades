"""changed the school name to mirio_students

Revision ID: ce6d7a0377e5
Revises: 791279dd0760
Create Date: 2023-08-31 00:30:05.993141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ce6d7a0377e5"
down_revision = "791279dd0760"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table("mirio_students", "students")


def downgrade() -> None:
    op.rename_table("mirio_students", "students")
