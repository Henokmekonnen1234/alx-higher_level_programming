-- this query will create a database hbtn_0d_2
-- and will create user user_0d_2
-- the code must not fail if both exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
ON hbtn_0d_2_pwd
TO 'user_0d_2'@'localhost';
