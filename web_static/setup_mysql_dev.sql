-- prepares a MySQL server for the project

--  creating database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- creating new user hbnb_dev (in localhost)
CREATE USER IF NOT EXISTS
'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- granting privileges for:
-- all privileges on the database hbnb_dev_db (and only this database)
-- SELECT privilege on the database performance_schema (and only this database)
GRANT ALL
ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost';

GRANT SELECT
ON performance_schema.*
TO 'hbnb_dev'@'localhost';
