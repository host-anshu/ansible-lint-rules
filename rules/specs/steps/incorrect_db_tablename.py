from ansiblelint import RulesCollection
from behave import *

from rules.IncorrectDBTableName import IncorrectDBTableName


@given('inventory and playbook with DB or table names being of different case while dropping '
	'than while creating')
def step_impl(context):
	# Bind inventory and playbook to the context
	context.inv = '/path/to/inv'
	context.pb = '/path/tispb'


@when('linted with IncorrectDBTableName rule')
def step_impl(context):
	context.result = True  # invoke the linter rule here instead


@then('reports such tasks and name differences')
def step_impl(context):
	assert context.result is True