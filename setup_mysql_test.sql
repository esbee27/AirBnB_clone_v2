-- Creates a database and user with password
-- Creates a database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates a user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- Sets password for user
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
-- Grants all privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grants select privileges
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
