Feature: Conflicting vars
	Looks for vars with same name if we ignore case of the vars or we ignore the special 
	characters in them.

  	Scenario Outline: vars with same name using different cases
  		Given	inventory and playbook having vars <first> and <second>
  		When	linted with ConflictingVars rule
  		Then	reports "<first> and <second> vars are same if case ignored"

		Examples: Case Insensitive
		   | first 		| second 	|
		   | first 		| FIRST  	|
		   | titlecase 	| TitleCase |

  	Scenario Outline: vars with same name, if special characters ignored
  		Given	inventory and playbook having vars <first> and <second>
  		When	linted with ConflictingVars rule
  		Then	reports "<first> and <second> vars are same if special chars ignored"

		Examples: Special Characters
		   | first 		| second 	|
		   | firstvar 	| first_var |

  	Scenario Outline: vars with same name, if both case and special characters ignored
  		Given	inventory and playbook having vars <first> and <second>
  		When	linted with ConflictingVars rule
  		Then	reports "<first> and <second> vars are same if both case and special chars 
  				ignored"

		Examples: Case Insensitive and Special Characters
		   | first 		| second 	|
		   | firstvar 	| FIRST_VAR |
		   | firstVar 	| First_var |