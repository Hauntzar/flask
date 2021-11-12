"""empty message

Revision ID: e95bf76ceeec
Revises: 586af737dde3
Create Date: 2021-11-05 20:19:13.978217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e95bf76ceeec'
down_revision = '586af737dde3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('owners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('puppy_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['puppy_id'], ['puppies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('owners')
    # ### end Alembic commands ###
