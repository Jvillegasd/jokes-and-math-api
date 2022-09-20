"""Create Joke table

Revision ID: 1fda5185d745
Revises:
Create Date: 2022-09-20 03:33:59.671163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fda5185d745'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'joke',
        sa.Column('joke_id', sa.Integer(), nullable=False),
        sa.Column('phrase', sa.Text()),
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            default=sa.func.now(),
            nullable=False
        ),
        sa.Column(
            'updated_at',
            sa.DateTime(timezone=True),
            default=sa.func.now(),
            nullable=False
        ),
        sa.PrimaryKeyConstraint('joke_id', name=op.f('pk_joke')),
    )


def downgrade() -> None:
    op.drop_table('joke')
