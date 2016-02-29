"""Ansible-lint rule for undefined vars"""

from ansiblelint import AnsibleLintRule


class UndefinedVars(AnsibleLintRule):
    id = 'ANSIBLE0013'
    shortdesc = 'Var used in tasks is not defined'
    description = (
    	'Var being used in tasks is not defined as in group_vars or host_vars')
    tags = ['invalid_input', 'vars']

    def matchplaybook(self, playbook):
    	"""
    	Check if group_vars or host_vars being used are defined or not.
    	"""