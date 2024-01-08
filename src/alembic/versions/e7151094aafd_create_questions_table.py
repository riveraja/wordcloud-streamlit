"""create questions table

Revision ID: e7151094aafd
Revises: 
Create Date: 2024-01-07 17:47:56.996909

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e7151094aafd"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE TABLE IF NOT EXISTS questions (question TEXT);")


def downgrade() -> None:
    op.drop_table("questions")
