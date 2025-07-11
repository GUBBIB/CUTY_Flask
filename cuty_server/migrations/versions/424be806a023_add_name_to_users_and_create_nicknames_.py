"""add_name_to_users_and_create_nicknames_table

Revision ID: 424be806a023
Revises: 6a89c7f12da9
Create Date: 2025-01-21 20:06:21.659830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '424be806a023'
down_revision = '6a89c7f12da9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nicknames',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nickname')
    )
    with op.batch_alter_table('post_comments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('anonymous_nickname', sa.String(length=100), nullable=False))

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nickname', sa.String(length=100), nullable=False))

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=100), nullable=False))
        batch_op.drop_constraint('users_nickname_key', type_='unique')
        batch_op.drop_column('nickname')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nickname', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
        batch_op.create_unique_constraint('users_nickname_key', ['nickname'])
        batch_op.drop_column('name')

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('nickname')

    with op.batch_alter_table('post_comments', schema=None) as batch_op:
        batch_op.drop_column('anonymous_nickname')

    op.drop_table('nicknames')
    # ### end Alembic commands ###
