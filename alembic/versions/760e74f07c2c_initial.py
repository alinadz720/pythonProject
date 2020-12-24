"""Initial

Revision ID: 760e74f07c2c
Revises: 
Create Date: 2020-12-06 21:08:14.880186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '760e74f07c2c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('status', sa.Enum('available', 'pending', 'sold', name='productstatus'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('firstname', sa.String(length=64), nullable=True),
    sa.Column('lastname', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('productId', sa.Integer(), nullable=True),
    sa.Column('status', sa.Enum('placed', 'approved', 'delivered', name='orderstatus'), nullable=True),
    sa.Column('is_complete', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['productId'], ['Products.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Orders')
    op.drop_table('Users')
    op.drop_table('Products')
    # ### end Alembic commands ###