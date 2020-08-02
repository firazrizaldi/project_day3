"""create table toys

Revision ID: 71491cb6d274
Revises: 9281d287cf05
Create Date: 2020-08-03 01:05:40.246165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71491cb6d274'
down_revision = '9281d287cf05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('toys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.Text(), nullable=True),
    sa.Column('puppy_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['puppy_id'], ['puppies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('toys')
    # ### end Alembic commands ###
