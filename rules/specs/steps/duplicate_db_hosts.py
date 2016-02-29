from ansiblelint import RulesCollection
from behave import *

from rules.DuplicateDBHost import DuplicateDBHost


@given('inventory and playbook with same DB host listed more than once')
def step_impl(context):
	# Bind inventory and playbook to the context
	context.inv = '/path/to/inv'
	context.pb = '/path/tispb'


@when('linted with DuplicateDBHost rule')
def step_impl(context):
	context.result = True  # invoke the linter rule here instead


@then('reports such inventories or plays')
def step_impl(context):
	assert context.result is True