"""empty message

Revision ID: 223b8502c8e
Revises: 4a66c6215b0
Create Date: 2015-08-24 21:12:02.894641

"""

# revision identifiers, used by Alembic.
revision = '223b8502c8e'
down_revision = '4a66c6215b0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pokemon_moves', sa.Column('id', sa.Integer(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pokemon_moves', 'id')
    ### end Alembic commands ###
