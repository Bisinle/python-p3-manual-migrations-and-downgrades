"""k_e_m_u name taken 

Revision ID: fd890b1be45d
Revises: da4b5df0bccf
Create Date: 2023-08-31 00:50:12.110978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fd890b1be45d"
down_revision = "da4b5df0bccf"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table("moringa", "k_e_m_u")


def downgrade() -> None:
    op.rename_table("k_e_m_u", "moringa")
