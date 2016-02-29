Feature: Different case DB and table name
	Looks for DB or tables that are being dropped and created with their names in different 
	cases

  	Scenario Outline: different case DB and table name when dropped and created
  		Given	inventory and playbook with names of <type> dropped as <drop_name> and that of 
  				created as <create_name>
  		When	linted with IncorrectDBTableName rule
  		Then	reports such tasks and name differences

		Examples: Different Case
		   | type 		| drop_name 	| create_name 	|
		   | DB 		| test		  	| TEST 			|
		   | table 		| test_table	| TEST_TABLE 	|