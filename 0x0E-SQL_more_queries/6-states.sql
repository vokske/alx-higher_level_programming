-- Creates a database and table on my MYSQL server
-- Values in 'id' column must be unique, auto-generated, and can't be null.
-- The id value is to be used as the primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY, name VARCHAR(256) NOT NULL);

