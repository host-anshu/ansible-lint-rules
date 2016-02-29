"""Ansible-lint rule for invalid image"""

from ansiblelint import AnsibleLintRule


class InvalidImage(AnsibleLintRule):
    id = 'ANSIBLE00012'
    shortdesc = 'Image URL inaccessible'
    description = (
    	'Image url is wrong or is not accessible using the given credentials')
    tags = ['image', 'invalid_input']

    def matchplaybook(self, playbook):
    	"""
    	Check if images defined exist and are accessible using the given credentials.
    	"""