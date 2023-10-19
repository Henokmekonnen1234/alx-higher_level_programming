-- this query will create user_0d_1 if it exists the code must not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
ON *.* TO 'user_0d_1'@'localhost';
