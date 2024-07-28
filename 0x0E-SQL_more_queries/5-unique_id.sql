-- Creates another table on my MYSQL server
-- One column of the table should have a default value that must be unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT '1' UNIQUE, name VARCHAR(256));

