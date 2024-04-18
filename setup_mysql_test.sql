-- Create a database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
USE hbnb_test_db;

-- Grant all priveledge to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant select privileges to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
