"""Ansible-lint rule for mismatching DB and Table names during drop and create"""

from ansiblelint import AnsibleLintRule


# DropCreateNameMismatch?
class IncorrectDBTableName(AnsibleLintRule):
    id = 'ANSIBLE0011'
    shortdesc = 'Drop and create name mismatch'
    description = \
    	'Name used while dropping and creating must be case sensitive.'
    tags = ['db']

    def matchplaybook(self, playbook):
    	"""
    	Check if names used while dropping and creating are case sensitive. 
    	"""