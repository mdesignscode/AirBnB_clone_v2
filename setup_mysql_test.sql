-- prepares a MySQL server for the project

-- creating the database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- creating a new user hbnb_test (in localhost)
CREATE USER IF NOT EXISTS
'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- granting privilges on:
-- all privileges on the database hbnb_test_db (and only this database)
-- SELECT privilege on the database performance_schema (and only this database)
GRANT ALL
ON hbnb_test_db.*
TO 'hbnb_test'@'localhost';

GRANT SELECT
ON performance_schema.*
TO 'hbnb_test'@'localhost';
