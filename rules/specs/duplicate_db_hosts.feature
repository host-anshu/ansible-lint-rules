Feature: Duplicate DB Host
	Looks for duplicate DB hosts to avoid DB instructions run more than once

  	Scenario: same DB host listed more than once
  		Given	inventory and playbook with same DB host listed more than once
  		When	linted with DuplicateDBHost rule
  		Then	reports such inventories or plays