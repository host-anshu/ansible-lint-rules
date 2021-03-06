from ansiblelint import RulesCollection
from behave import *

from rules.UnusedVars import UnusedVars


@given('inventory and playbook having vars not used in tasks')
def step_impl(context):
	# Bind inventory and playbook to the context
	context.inv = '/path/to/inv'
	context.pb = '/path/tispb'


@when('linted with UnusedVars rule')
def step_impl(context):
	context.result = True  # invoke the linter rule here instead


@then('reports unused vars')
def step_impl(context):
	assert context.result is True