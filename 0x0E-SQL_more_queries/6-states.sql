-- Creates a database and a table in the database in MySQL server

-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create the table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
name VARCHAR(256) NOT NULL);
