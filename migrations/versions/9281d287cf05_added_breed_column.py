"""added breed column

Revision ID: 9281d287cf05
Revises: 
Create Date: 2020-08-03 00:47:06.894392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9281d287cf05'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('puppies', sa.Column('breed', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('puppies', 'breed')
    # ### end Alembic commands ###