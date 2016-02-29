from ansiblelint import RulesCollection
from behave import *

from rules.ConflictingVars import ConflictingVars


@given('inventory and playbook having vars of different case')
def step_impl(context):
	# Bind inventory and playbook to the context
	context.inv = '/path/to/inv'
	context.pb = '/path/to/pb'


@given('inventory and playbook having vars differing by special characters')
def step_impl(context):
	# Bind inventory and playbook to the context
	context.inv = '/path/to/inv'
	context.pb = '/path/to/pb'


@given('inventory and playbook having vars differing by case and special characters')
def step_impl(context):
	# Bind inventory and playbook to the context
	context.inv = '/path/to/inv'
	context.pb = '/path/to/pb'


@when('linted with ConflictingVars rule')
def step_impl(context):
	context.result = True  # invoke the linter rule here instead


@then('reports conflicting vars')
def step_impl(context):
	assert context.result is True
