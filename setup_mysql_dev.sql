-- Creates a database and user with password
-- Creates a database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates a user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- Sets password for user
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- Grants all privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grants select privileges
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
