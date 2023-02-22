-- Creates a database and a table in the database in MySQL server

-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create the table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY (state_id) REFERENCES states(id));
