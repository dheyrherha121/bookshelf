"""add addedBooks table

Revision ID: fb8bdfe9ff19
Revises: 
Create Date: 2024-04-15 16:58:49.356461

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb8bdfe9ff19'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('AddedBooks',
                    sa.Column('PublicationDate', sa.String, nullable=False,),
                    sa.Column('id', sa.Integer, primary_key=True, nullable=False),
                    sa.Column('title', sa.String, nullable=False),
                    sa.Column('ISBN', sa.Integer, nullable=False),
                    sa.Column('Author', sa.String, nullable=False))


def downgrade() -> None:
    op.drop_table('AddedBooks')
