"""Ansible-lint rule for conflicting vars"""

from ansiblelint import AnsibleLintRule


class ConflictingVars(AnsibleLintRule):
    id = 'ANSIBLE0009'
    shortdesc = 'Case-insensitive and special chars ignored vars names must be unique'
    description = (
    	'Case-insensitive and special characters ignored group_vars or host_vars '
    	'must be uniquely defined')
    tags = ['repeatability', 'vars']

    def matchplaybook(self, playbook):
    	"""
    	Check if group_vars or host_vars are uniquely defined if case and special chars 
    	in their names are ignored.
    	"""