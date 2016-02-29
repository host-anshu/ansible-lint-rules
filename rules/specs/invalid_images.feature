Feature: Invalid image
	Looks for images that don't exist or are not accessible with the given credentials

  	Scenario: image absent
  		Given inventory and playbook using images that don't exist
  		When linted with InvalidImage rule
  		Then reports such images

  	Scenario: image inaccessible
  		Given inventory and playbook using images that aren't accessible by the mentioned credentials
  		When linted with InvalidImage rule
  		Then reports such images