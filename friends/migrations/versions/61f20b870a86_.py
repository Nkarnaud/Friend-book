"""empty message

Revision ID: 61f20b870a86
Revises: 
Create Date: 2019-02-28 23:37:03.775249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61f20b870a86'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currencyData',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('currency_code', sa.String(length=250), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('currency_price', sa.Integer(), nullable=False),
    sa.Column('insert_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('currencyData')
    # ### end Alembic commands ###
