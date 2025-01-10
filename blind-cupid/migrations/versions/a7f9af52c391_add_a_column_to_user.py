"""Add a column to user

Revision ID: a7f9af52c391
Revises: 40b0acfda2b5
Create Date: 2025-01-10 12:07:33.983608

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7f9af52c391'
down_revision: Union[str, None] = '40b0acfda2b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

#alembic upgrade head -> updates the schema running the specified Alembic directives (DDL)
def upgrade() -> None:
    op.add_column('user', sa.Column('fav_food', sa.String))

#Ran when executing 'alembic downgrade base'
def downgrade() -> None:
    op.drop_column('user', 'fav_food')
