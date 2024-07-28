-- Creates a table in a database in my MYSQL server
-- Specifies the state_id as a foreign key 
-- This key references to id of the states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	CONSTRAINT FOREIGN KEY (state_id) REFERENCES states (id));

