"""password hashing

Revision ID: 757e867c1787
Revises: 1d949b68b6d9
Create Date: 2022-01-06 21:50:40.633038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '757e867c1787'
down_revision = '1d949b68b6d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'store_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'store_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
