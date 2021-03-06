"""empty message

Revision ID: b742f875c673
Revises: 456c10bae7a4
Create Date: 2018-06-10 20:18:55.628521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b742f875c673'
down_revision = '456c10bae7a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'tb_resources_relationships', 'tb_postmeta', ['object_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'tb_resources_relationships', 'tb_resources', ['resources_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'tb_role_admin', 'tb_admin', ['admin_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'tb_role_admin', 'tb_role', ['role_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'tb_term_relationships', 'tb_postmeta', ['object_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'tb_term_relationships', 'tb_term_taxonomy', ['term_taxonomy_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tb_term_relationships', type_='foreignkey')
    op.drop_constraint(None, 'tb_term_relationships', type_='foreignkey')
    op.drop_constraint(None, 'tb_role_admin', type_='foreignkey')
    op.drop_constraint(None, 'tb_role_admin', type_='foreignkey')
    op.drop_constraint(None, 'tb_resources_relationships', type_='foreignkey')
    op.drop_constraint(None, 'tb_resources_relationships', type_='foreignkey')
    # ### end Alembic commands ###
