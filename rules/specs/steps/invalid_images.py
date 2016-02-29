from ansiblelint import RulesCollection
from behave import *

from rules.InvalidImage import InvalidImage


@given('inventory and playbook using images that don\'t exist')
def step_impl(context):
	# Bind inventory and playbook to the context
	context.inv = '/path/to/inv'
	context.pb = '/path/to/pb'


@given('inventory and playbook using images that aren\'t accessible by the mentioned credentials')
def step_impl(context):
	# Bind inventory and playbook to the context
	context.inv = '/path/to/inv'
	context.pb = '/path/to/pb'


@when('linted with InvalidImage rule')
def step_impl(context):
	context.result = True  # invoke the linter rule here instead


@then('reports such images')
def step_impl(context):
	assert context.result is True
