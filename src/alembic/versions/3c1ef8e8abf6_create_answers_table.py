"""create answers table

Revision ID: 3c1ef8e8abf6
Revises: e7151094aafd
Create Date: 2024-01-07 17:51:51.566728

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c1ef8e8abf6'
down_revision: Union[str, None] = 'e7151094aafd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('CREATE TABLE IF NOT EXISTS answers (qid INTEGER, answer TEXT);')


def downgrade() -> None:
    op.drop_table('answers')
