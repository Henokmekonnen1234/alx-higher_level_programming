-- this will create id__not_null table 
CREATE TABLE IF NOT EXiSTS id_not_null
(
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256)
);
