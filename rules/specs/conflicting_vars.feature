Feature: Conflicting vars
	Looks for vars with same name if we ignore case of the vars or we ignore the special 
	characters in them.

  	Scenario: vars with same name using different cases
  		Given inventory and playbook having vars of different case
  		When linted with ConflictingVars rule
  		Then reports conflicting vars

  	Scenario: vars with same name, if special characters ignored
  		Given inventory and playbook having vars differing by special characters
  		When linted with ConflictingVars rule
  		Then reports conflicting vars

  	Scenario: vars with same name, if both case and special characters ignored
  		Given inventory and playbook having vars differing by case and special characters
  		When linted with ConflictingVars rule
  		Then reports conflicting vars