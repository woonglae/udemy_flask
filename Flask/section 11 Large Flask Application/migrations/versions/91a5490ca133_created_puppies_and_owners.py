"""created puppies and owners

Revision ID: 91a5490ca133
Revises: 
Create Date: 2019-06-28 22:22:47.700296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91a5490ca133'
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
    op.create_table('owners',
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('pup_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pup_id'], ['puppies.id'], ),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('owners')
    op.drop_table('puppies')
    # ### end Alembic commands ###