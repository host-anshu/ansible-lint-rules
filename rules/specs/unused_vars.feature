Feature: Unused vars
	Looks for group_vars or host_vars that are not used in tasks.

  	Scenario: var defined either as group_vars or host_vars but not used in tasks
  		Given inventory and playbook having vars not used in tasks
  		When linted with UnusedVars rule
  		Then reports unused vars