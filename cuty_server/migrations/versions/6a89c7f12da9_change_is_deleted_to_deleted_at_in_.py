"""change is_deleted to deleted_at in posts and comments

Revision ID: 6a89c7f12da9
Revises: b788863ba985
Create Date: 2025-01-17 16:31:56.500921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a89c7f12da9'
down_revision = 'b788863ba985'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post_comments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deleted_at', sa.DateTime(), nullable=True))
        batch_op.drop_column('is_deleted')

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deleted_at', sa.DateTime(), nullable=True))
        batch_op.drop_column('is_deleted')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.drop_column('deleted_at')

    with op.batch_alter_table('post_comments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.drop_column('deleted_at')

    # ### end Alembic commands ###
