"""Create relationshipe for User to Profile

Revision ID: 03972d751223
Revises: a37ac459f946
Create Date: 2025-04-23 11:50:39.023670

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03972d751223'
down_revision: Union[str, None] = 'a37ac459f946'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('suname', sa.String(), nullable=True),
    sa.Column('about', sa.String(), nullable=True),
    sa.Column('date_birthday', sa.DateTime(), nullable=True),
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=False),
    sa.Column('update_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    # ### end Alembic commands ###
