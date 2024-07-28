-- Create a MYSQL server user
-- Grants that user all privileges on the MYSQL server
-- Sets the password for the user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

