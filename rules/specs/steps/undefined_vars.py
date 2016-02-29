from ansiblelint import RulesCollection
from behave import *

from rules.UndefinedVars import UndefinedVars


@given('inventory and playbook having tasks using undefined group_vars or host_vars')
def step_impl(context):
	# Bind inventory and playbook to the context
	context.inv = '/path/to/inv'
	context.pb = '/path/to/pb'


@then('reports tasks and the undefined vars')
def step_impl(context):
	assert context.result is True


@given('inventory and playbook having tasks with vars defined both in group_vars and host_vars')
def step_impl(context):
	# Bind inventory and playbook to the context
	context.inv = '/path/to/inv'
	context.pb = '/path/to/pb'


@then('reports the variables defined at multiple places')
def step_impl(context):
	assert context.result is True


@when('linted with UndefinedVars rule')
def step_impl(context):
	# invoke the linter rule here.
	context.result = True  # invoke the linter rule here instead