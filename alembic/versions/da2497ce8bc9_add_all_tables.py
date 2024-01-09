"""add all tables

Revision ID: da2497ce8bc9
Revises: 
Create Date: 2023-12-06 10:55:11.848035

"""
from typing import Sequence, Union
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da2497ce8bc9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tank_ukraine',
        sa.Column('tank_ukraine_id', sa.Integer, primary_key=True, autoincrement=True, unique=True,),
        sa.Column('total', sa.Integer, nullable=False,),
        sa.Column('destroyed', sa.Integer, nullable=False,),
        sa.Column('damaged', sa.Integer, nullable=False,),
        sa.Column('abandoned', sa.Integer, nullable=False,),
        sa.Column('captured', sa.Integer, nullable=False,),
        sa.Column('scraped_at', sa.DateTime, unique=True),
        sa.Column('created_at', sa.DateTime(timezone=True,), default=datetime.utcnow, nullable=False),
        )


    op.create_table(
        'afv_ukraine',
        sa.Column('afv_ukraine_id', sa.Integer, primary_key=True, autoincrement=True, unique=True,),
        sa.Column('total', sa.Integer, nullable=False,),
        sa.Column('destroyed', sa.Integer, nullable=False,),
        sa.Column('damaged', sa.Integer, nullable=False,),
        sa.Column('abandoned', sa.Integer, nullable=False,),
        sa.Column('captured', sa.Integer, nullable=False,),
        sa.Column('scraped_at', sa.DateTime, unique=True),
        sa.Column('created_at', sa.DateTime(timezone=True,), default=datetime.utcnow, nullable=False),
        )

    op.create_table(
        'ifv_ukraine',
        sa.Column('ifv_ukraine_id', sa.Integer, primary_key=True, autoincrement=True, unique=True,),
        sa.Column('total', sa.Integer, nullable=False,),
        sa.Column('destroyed', sa.Integer, nullable=False,),
        sa.Column('damaged', sa.Integer, nullable=False,),
        sa.Column('abandoned', sa.Integer, nullable=False,),
        sa.Column('captured', sa.Integer, nullable=False,),
        sa.Column('scraped_at', sa.DateTime, unique=True),
        sa.Column('created_at', sa.DateTime(timezone=True,), default=datetime.utcnow, nullable=False),
        )

    op.create_table(
        'apc_ukraine',
        sa.Column('apc_ukraine_id', sa.Integer, primary_key=True, autoincrement=True, unique=True,),
        sa.Column('total', sa.Integer, nullable=False,),
        sa.Column('destroyed', sa.Integer, nullable=False,),
        sa.Column('damaged', sa.Integer, nullable=False,),
        sa.Column('abandoned', sa.Integer, nullable=False,),
        sa.Column('captured', sa.Integer, nullable=False,),
        sa.Column('scraped_at', sa.DateTime, unique=True),
        sa.Column('created_at', sa.DateTime(timezone=True,), default=datetime.utcnow, nullable=False),
        )


    op.create_table(
        'imv_ukraine',
        sa.Column('imv_ukraine_id', sa.Integer, primary_key=True, autoincrement=True, unique=True,),
        sa.Column('total', sa.Integer, nullable=False,),
        sa.Column('destroyed', sa.Integer, nullable=False,),
        sa.Column('damaged', sa.Integer, nullable=False,),
        sa.Column('abandoned', sa.Integer, nullable=False,),
        sa.Column('captured', sa.Integer, nullable=False,),
        sa.Column('scraped_at', sa.DateTime, unique=True),
        sa.Column('created_at', sa.DateTime(timezone=True,), default=datetime.utcnow, nullable=False),
        )

    #----------------------------------------------------------------------------------------------------

    op.create_table(
        'tank_russia',
        sa.Column('tank_russia_id', sa.Integer, primary_key=True, autoincrement=True, unique=True,),
        sa.Column('total', sa.Integer, nullable=False,),
        sa.Column('destroyed', sa.Integer, nullable=False,),
        sa.Column('damaged', sa.Integer, nullable=False,),
        sa.Column('abandoned', sa.Integer, nullable=False,),
        sa.Column('captured', sa.Integer, nullable=False,),
        sa.Column('scraped_at', sa.DateTime, unique=True),
        sa.Column('created_at', sa.DateTime(timezone=True,), default=datetime.utcnow, nullable=False),
        )


    op.create_table(
        'afv_russia',
        sa.Column('afv_russia_id', sa.Integer, primary_key=True, autoincrement=True, unique=True,),
        sa.Column('total', sa.Integer, nullable=False,),
        sa.Column('destroyed', sa.Integer, nullable=False,),
        sa.Column('damaged', sa.Integer, nullable=False,),
        sa.Column('abandoned', sa.Integer, nullable=False,),
        sa.Column('captured', sa.Integer, nullable=False,),
        sa.Column('scraped_at', sa.DateTime, unique=True),
        sa.Column('created_at', sa.DateTime(timezone=True,), default=datetime.utcnow, nullable=False),
        )

    op.create_table(
        'ifv_russia',
        sa.Column('ifv_russia_id', sa.Integer, primary_key=True, autoincrement=True, unique=True,),
        sa.Column('total', sa.Integer, nullable=False,),
        sa.Column('destroyed', sa.Integer, nullable=False,),
        sa.Column('damaged', sa.Integer, nullable=False,),
        sa.Column('abandoned', sa.Integer, nullable=False,),
        sa.Column('captured', sa.Integer, nullable=False,),
        sa.Column('scraped_at', sa.DateTime, unique=True),
        sa.Column('created_at', sa.DateTime(timezone=True,), default=datetime.utcnow, nullable=False),
        )

    op.create_table(
        'apc_russia',
        sa.Column('apc_russia_id', sa.Integer, primary_key=True, autoincrement=True, unique=True,),
        sa.Column('total', sa.Integer, nullable=False,),
        sa.Column('destroyed', sa.Integer, nullable=False,),
        sa.Column('damaged', sa.Integer, nullable=False,),
        sa.Column('abandoned', sa.Integer, nullable=False,),
        sa.Column('captured', sa.Integer, nullable=False,),
        sa.Column('scraped_at', sa.DateTime, unique=True),
        sa.Column('created_at', sa.DateTime(timezone=True,), default=datetime.utcnow, nullable=False),
        )


    op.create_table(
        'imv_russia',
        sa.Column('imv_russia_id', sa.Integer, primary_key=True, autoincrement=True, unique=True,),
        sa.Column('total', sa.Integer, nullable=False,),
        sa.Column('destroyed', sa.Integer, nullable=False,),
        sa.Column('damaged', sa.Integer, nullable=False,),
        sa.Column('abandoned', sa.Integer, nullable=False,),
        sa.Column('captured', sa.Integer, nullable=False,),
        sa.Column('scraped_at', sa.DateTime, unique=True),
        sa.Column('created_at', sa.DateTime(timezone=True,), default=datetime.utcnow, nullable=False),
        )


def downgrade() -> None:
    # Drop tables - Ukraine.
    op.drop_table('tank_ukraine')
    op.drop_table('afv_ukraine')
    op.drop_table('ifv_ukraine')
    op.drop_table('apc_ukraine')
    op.drop_table('imv_ukraine')

    # Drop tables - Russia.
    op.drop_table('tank_russia')
    op.drop_table('afv_russia')
    op.drop_table('ifv_russia')
    op.drop_table('apc_russia')
    op.drop_table('imv_russia')
