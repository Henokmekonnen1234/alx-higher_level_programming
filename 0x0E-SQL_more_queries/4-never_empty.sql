-- this will create id__not_null table 
CREATE TABLE IF NOT EXiSTS id_not_null
(
	id INT UNIQUE NOT NULL DEFAULT 1 PRIMARY KEY,
	name VARCHAR(256)
);
