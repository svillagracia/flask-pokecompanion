"""empty message

Revision ID: 1ae136f4e3e
Revises: 2fcb59acffc
Create Date: 2015-08-25 13:52:19.580698

"""

# revision identifiers, used by Alembic.
revision = '1ae136f4e3e'
down_revision = '2fcb59acffc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon_moves',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pokemon_id', sa.Integer(), nullable=True),
    sa.Column('move_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['move_id'], ['moves.id'], ),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokemon_moves')
    ### end Alembic commands ###
