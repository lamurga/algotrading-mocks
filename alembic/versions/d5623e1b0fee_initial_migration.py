"""Initial migration

Revision ID: d5623e1b0fee
Revises: 
Create Date: 2024-10-28 05:19:29.198488

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5623e1b0fee'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('asset_manager_risk_profile',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('asset_manager_id', sa.Integer(), nullable=True),
    sa.Column('risk_profile_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('broker',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exchange',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('open_from', sa.DateTime(), nullable=True),
    sa.Column('open_until', sa.DateTime(), nullable=True),
    sa.Column('country_code', sa.String(), nullable=True),
    sa.Column('symbol', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('strategy_params',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('operational_hours', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('account',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('number', sa.String(), nullable=False),
    sa.Column('account_type', sa.String(), nullable=False),
    sa.Column('currency', sa.String(), nullable=True),
    sa.Column('initial_balance', sa.Float(precision=53), nullable=True),
    sa.Column('current_balance', sa.Float(precision=53), nullable=True),
    sa.Column('margin_available', sa.Float(precision=53), nullable=True),
    sa.Column('unrealized_pnl', sa.Float(precision=53), nullable=True),
    sa.Column('realized_pnl', sa.Float(precision=53), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('action_change',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('ticker', sa.String(), nullable=True),
    sa.Column('exchange', sa.String(), nullable=True),
    sa.Column('country_code', sa.String(), nullable=True),
    sa.Column('type_value', sa.String(), nullable=True),
    sa.Column('currency', sa.String(), nullable=True),
    sa.Column('isin', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('at_group',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('performance', sa.Text(), nullable=True),
    sa.Column('symbol_distribution', sa.Text(), nullable=True),
    sa.Column('symbol', sa.Text(), nullable=True),
    sa.Column('strategies_composition', sa.Text(), nullable=True),
    sa.Column('strategy_distribution', sa.Text(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('risk_profile',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('min_score', sa.Numeric(), nullable=True),
    sa.Column('max_score', sa.Numeric(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('strategy',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('exchange_id', sa.Integer(), nullable=True),
    sa.Column('strategy_param_id', sa.Integer(), nullable=True),
    sa.Column('arn_location', sa.String(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('strategy_allocation',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('asset_allocation', sa.Float(precision=53), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('symbol',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('ticker', sa.String(), nullable=True),
    sa.Column('exchange', sa.String(), nullable=True),
    sa.Column('country_code', sa.String(), nullable=True),
    sa.Column('type_value', sa.String(), nullable=True),
    sa.Column('currency', sa.String(), nullable=True),
    sa.Column('isin', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('account_strategy_position',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('strategy_id', sa.Integer(), nullable=True),
    sa.Column('symbol', sa.String(), nullable=True),
    sa.Column('contract_symbol', sa.Integer(), nullable=True),
    sa.Column('currency', sa.String(), nullable=True),
    sa.Column('position', sa.String(), nullable=True),
    sa.Column('average_cost', sa.String(), nullable=True),
    sa.Column('additional_info', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.ForeignKeyConstraint(['strategy_id'], ['strategy.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('account_summary',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('account_type', sa.String(), nullable=True),
    sa.Column('net_liquidation', sa.Numeric(), nullable=True),
    sa.Column('total_cash_value', sa.Numeric(), nullable=True),
    sa.Column('settled_cash', sa.Numeric(), nullable=True),
    sa.Column('accrued_cash', sa.Numeric(), nullable=True),
    sa.Column('buying_power', sa.Numeric(), nullable=True),
    sa.Column('gross_position_value', sa.Numeric(), nullable=True),
    sa.Column('available_funds', sa.Numeric(), nullable=True),
    sa.Column('full_maint_margin_req', sa.Numeric(), nullable=True),
    sa.Column('full_available_funds', sa.Numeric(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('account_value',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('cash_balance', sa.Numeric(), nullable=True),
    sa.Column('realized_pnl', sa.Numeric(), nullable=True),
    sa.Column('unrealized_pnl', sa.Numeric(), nullable=True),
    sa.Column('market_value', sa.Numeric(), nullable=True),
    sa.Column('currency', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('group_risk_profile',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('risk_profile_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['at_group.id'], ),
    sa.ForeignKeyConstraint(['risk_profile_id'], ['risk_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_order',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('account_number', sa.String(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('parent_perm_id', sa.Integer(), nullable=True),
    sa.Column('perm_id', sa.Integer(), nullable=True),
    sa.Column('exchange', sa.String(), nullable=True),
    sa.Column('currency', sa.String(), nullable=True),
    sa.Column('contract_id', sa.String(), nullable=True),
    sa.Column('action', sa.String(), nullable=True),
    sa.Column('order_id', sa.String(), nullable=True),
    sa.Column('symbol', sa.String(), nullable=True),
    sa.Column('order_type', sa.String(), nullable=True),
    sa.Column('price', sa.Float(precision=53), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('lmt_price', sa.Float(precision=53), nullable=True),
    sa.Column('aux_price', sa.Float(precision=53), nullable=True),
    sa.Column('tif', sa.String(), nullable=True),
    sa.Column('filled', sa.Integer(), nullable=True),
    sa.Column('avg_fill_price', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('strategy_strategy_allocation',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('strategy_id', sa.Integer(), nullable=True),
    sa.Column('strategy_allocation_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['strategy_allocation_id'], ['strategy_allocation.id'], ),
    sa.ForeignKeyConstraint(['strategy_id'], ['strategy.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('symbol_action_change',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('symbol_id', sa.Integer(), nullable=True),
    sa.Column('action_change_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['action_change_id'], ['action_change.id'], ),
    sa.ForeignKeyConstraint(['symbol_id'], ['symbol.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_risk_profile',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('risk_profile_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['risk_profile_id'], ['risk_profile.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('error_log',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('broker_id', sa.Integer(), nullable=True),
    sa.Column('broker_group_id', sa.Integer(), nullable=True),
    sa.Column('risk_profile_id', sa.Integer(), nullable=True),
    sa.Column('strategy_id', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('error_message', sa.String(), nullable=True),
    sa.Column('error_datetime', sa.DateTime(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Numeric(), nullable=True),
    sa.Column('currency', sa.String(), nullable=True),
    sa.Column('position_type', sa.String(), nullable=True),
    sa.Column('asset_allocation', sa.String(), nullable=True),
    sa.Column('error_type', sa.String(), nullable=True),
    sa.Column('current_condition', sa.String(), nullable=True),
    sa.Column('set_condition', sa.String(), nullable=True),
    sa.Column('gap', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.ForeignKeyConstraint(['broker_group_id'], ['at_group.id'], ),
    sa.ForeignKeyConstraint(['broker_id'], ['broker.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order_order.id'], ),
    sa.ForeignKeyConstraint(['risk_profile_id'], ['risk_profile.id'], ),
    sa.ForeignKeyConstraint(['strategy_id'], ['strategy.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_fills',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('execution_id', sa.String(), nullable=True),
    sa.Column('contract_id', sa.String(), nullable=True),
    sa.Column('commission', sa.Float(precision=53), nullable=True),
    sa.Column('currency', sa.String(), nullable=True),
    sa.Column('released_pnl', sa.Float(precision=53), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order_order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_log',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('open_order', sa.Boolean(), nullable=False),
    sa.Column('broker_id', sa.Integer(), nullable=False),
    sa.Column('broker_name', sa.String(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.Column('profile_name', sa.String(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('group_name', sa.String(), nullable=False),
    sa.Column('strategy_id', sa.Integer(), nullable=False),
    sa.Column('strategy_name', sa.String(), nullable=False),
    sa.Column('account_number', sa.String(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('contract_symbol', sa.String(), nullable=False),
    sa.Column('contract_id', sa.Integer(), nullable=False),
    sa.Column('action', sa.String(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('order_type', sa.String(), nullable=False),
    sa.Column('stop_price', sa.Float(precision=53), nullable=True),
    sa.Column('order_status', sa.String(), nullable=False),
    sa.Column('filled', sa.Integer(), nullable=False),
    sa.Column('remaining', sa.Integer(), nullable=False),
    sa.Column('avg_fill_price', sa.Float(precision=53), nullable=False),
    sa.Column('currency', sa.String(), nullable=False),
    sa.Column('exchange', sa.String(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('perm_id', sa.Integer(), nullable=False),
    sa.Column('total_commissions', sa.Float(precision=53), nullable=False),
    sa.Column('commission_currency', sa.String(), nullable=False),
    sa.Column('net_trade_pnl', sa.Integer(), nullable=True),
    sa.Column('lag_time', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('direction_long', sa.String(), nullable=False),
    sa.Column('direction_short', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['broker_id'], ['broker.id'], ),
    sa.ForeignKeyConstraint(['group_id'], ['at_group.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order_order.id'], ),
    sa.ForeignKeyConstraint(['profile_id'], ['risk_profile.id'], ),
    sa.ForeignKeyConstraint(['strategy_id'], ['strategy.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('signals',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('symbol', sa.String(), nullable=True),
    sa.Column('signal_type', sa.String(), nullable=True),
    sa.Column('strategy', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order_order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('signals')
    op.drop_table('order_log')
    op.drop_table('order_fills')
    op.drop_table('error_log')
    op.drop_table('user_risk_profile')
    op.drop_table('symbol_action_change')
    op.drop_table('strategy_strategy_allocation')
    op.drop_table('order_order')
    op.drop_table('group_risk_profile')
    op.drop_table('account_value')
    op.drop_table('account_summary')
    op.drop_table('account_strategy_position')
    op.drop_table('symbol')
    op.drop_table('strategy_allocation')
    op.drop_table('strategy')
    op.drop_table('risk_profile')
    op.drop_table('at_group')
    op.drop_table('action_change')
    op.drop_table('account')
    op.drop_table('user')
    op.drop_table('strategy_params')
    op.drop_table('exchange')
    op.drop_table('broker')
    op.drop_table('asset_manager_risk_profile')
    # ### end Alembic commands ###
