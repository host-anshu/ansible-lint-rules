Feature: Different case DB and table name
	Looks for DB or tables that are being dropped and created with their names in different 
	cases

  	Scenario: different case DB and table name when dropped and created
  		Given inventory and playbook with DB or table names being of different case while dropping than while creating
  		When linted with IncorrectDBTableName rule
  		Then reports such tasks and name differences