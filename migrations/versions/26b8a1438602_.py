"""empty message

Revision ID: 26b8a1438602
Revises: ec7d4c35740b
Create Date: 2016-07-24 09:45:40.779201

"""

# revision identifiers, used by Alembic.
revision = '26b8a1438602'
down_revision = 'ec7d4c35740b'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('trash_date', sa.DateTime(), nullable=True))
    op.add_column('events_version', sa.Column('trash_date', sa.DateTime(), autoincrement=False, nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events_version', 'trash_date')
    op.drop_column('events', 'trash_date')
    ### end Alembic commands ###
