"""add columns

Revision ID: 229125e67a92
Revises: 38e97104a486
Create Date: 2020-11-24 22:21:25.871105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "229125e67a92"
down_revision = "38e97104a486"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "users",
        sa.Column("is_active", sa.Boolean(), nullable=False),
    )


def downgrade():
    op.drop_column("users", "is_active")
