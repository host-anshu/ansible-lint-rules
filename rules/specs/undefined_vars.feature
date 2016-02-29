Feature: Undefined vars
	Looks for vars in tasks that hasn't been defined either as group vars or host vars

  	Scenario: var not defined either as group_vars or as host_vars
  		Given	inventory and playbook having tasks using undefined group_vars or host_vars
  		When	linted with UndefinedVars rule
  		Then	reports tasks and the undefined vars

  	Scenario: var defined both as group_vars or as host_vars
  		Given	inventory and playbook having tasks with vars defined both in group_vars and 
  				host_vars
  		When	linted with UndefinedVars rule
  		Then	reports the variables defined at multiple places