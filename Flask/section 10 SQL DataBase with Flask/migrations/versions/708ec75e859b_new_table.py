"""new table

Revision ID: 708ec75e859b
Revises: 
Create Date: 2019-06-27 22:53:20.626388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '708ec75e859b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('puppies')
    # ### end Alembic commands ###