"""Ansible-lint rule for duplicate DB hosts"""

from ansiblelint import AnsibleLintRule


class DuplicateDB(AnsibleLintRule):
    id = 'ANSIBLE0010'
    shortdesc = 'Duplicate DB host found'
    description = \
    	'Same DB host being used more than once. This would run DB steps more than once'
    tags = ['repeatability', 'db']

    def matchplaybook(self, playbook):
    	"""
    	Check if duplicate DB host being defined in inventory or playbook. 
    	"""