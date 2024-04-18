"""remove column

Revision ID: 4d03744cee11
Revises: fb8bdfe9ff19
Create Date: 2024-04-18 12:48:20.489362

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4d03744cee11'
down_revision: Union[str, None] = 'fb8bdfe9ff19'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('AddedBooks', 'PublicationDate')


def downgrade() -> None:
    pass
