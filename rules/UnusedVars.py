"""Ansible-lint rule for unused vars"""

from ansiblelint import AnsibleLintRule


class UnusedVars(AnsibleLintRule):
    id = 'ANSIBLE0014'
    shortdesc = 'Var defined is not being used'
    description = (
    	'Var being defined in group_vars or host_vars is not being used in any task.')
    tags = ['unused', 'vars']

    def matchplaybook(self, playbook):
    	"""
    	Check if playbook has variables define dthat aren't being used.
    	"""