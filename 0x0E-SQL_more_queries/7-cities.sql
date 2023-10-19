-- this query will create hbtn_0d_usa ad create table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	CONSTRAINT fk_state
	FOREIGN KEY (state_id)
	REFERECES states(id)
	[ON DELETE CASCADE]
	[ON UPDATE CASCADE]
);
