-- this query will create a database hbtn_0d_use and table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(
	id INT UNIQUE AUTO_INCREAMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
