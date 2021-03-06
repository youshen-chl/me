"""database v1.2

Revision ID: 24871ecda46d
Revises: None
Create Date: 2013-04-04 22:49:20.445000

"""

# revision identifiers, used by Alembic.
revision = '24871ecda46d'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('db_site_settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('version', sa.Float(), nullable=True),
    sa.Column('title', sa.String(length=512), nullable=True),
    sa.Column('subtitle', sa.String(length=128), nullable=True),
    sa.Column('copyright', sa.String(length=512), nullable=True),
    sa.Column('ga_tracking_id', sa.String(length=128), nullable=True),
    sa.Column('owner', sa.String(length=256), nullable=True),
    sa.Column('inited', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('db_stats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('target_type', sa.String(length=128), nullable=True),
    sa.Column('target_id', sa.Integer(), nullable=True),
    sa.Column('public', sa.Boolean(), nullable=True),
    sa.Column('view_count', sa.Integer(), nullable=True),
    sa.Column('share_count', sa.Integer(), nullable=True),
    sa.Column('like_count', sa.Integer(), nullable=True),
    sa.Column('unlike_count', sa.Integer(), nullable=True),
    sa.Column('post_count', sa.Integer(), nullable=True),
    sa.Column('photo_count', sa.Integer(), nullable=True),
    sa.Column('comment_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('db_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=True),
    sa.Column('nickname', sa.String(length=40), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('avatar', sa.String(length=512), nullable=True),
    sa.Column('role', sa.Enum('User', 'Admin', 'Owner'), nullable=True),
    sa.Column('joined_date', sa.DateTime(), nullable=True),
    sa.Column('_stats_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['_stats_id'], ['db_stats.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('db_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('_norm_name', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('post_count', sa.Integer(), nullable=True),
    sa.Column('_post_id_list', sa.Text(), nullable=True),
    sa.Column('_stats_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['_stats_id'], ['db_stats.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('db_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('sort', sa.Integer(), nullable=True),
    sa.Column('posts_per_page', sa.Integer(), nullable=True),
    sa.Column('order', sa.Enum('asc', 'desc'), nullable=True),
    sa.Column('template', sa.Enum('Timeline', 'List', 'Photo', 'Text'), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('_stats_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['_stats_id'], ['db_stats.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('db_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('public', sa.Boolean(), nullable=True),
    sa.Column('sticky', sa.Boolean(), nullable=True),
    sa.Column('post_date', sa.DateTime(), nullable=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('_stats_id', sa.Integer(), nullable=True),
    sa.Column('_tag_list', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['_stats_id'], ['db_stats.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['author_id'], ['db_user.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['category_id'], ['db_category.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('db_photo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('url', sa.String(length=1024), nullable=True),
    sa.Column('url_thumb', sa.String(length=1024), nullable=True),
    sa.Column('mime', sa.String(length=128), nullable=True),
    sa.Column('alt', sa.String(length=140), nullable=True),
    sa.Column('real_file', sa.String(length=1024), nullable=True),
    sa.Column('real_file_thumb', sa.String(length=1024), nullable=True),
    sa.Column('public', sa.Boolean(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('_stats_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['_stats_id'], ['db_stats.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['post_id'], ['db_post.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('db_comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('author', sa.String(length=32), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('_stats_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['_stats_id'], ['db_stats.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['post_id'], ['db_post.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('db_comment')
    op.drop_table('db_photo')
    op.drop_table('db_post')
    op.drop_table('db_category')
    op.drop_table('db_tag')
    op.drop_table('db_user')
    op.drop_table('db_stats')
    op.drop_table('db_site_settings')
    ### end Alembic commands ###
