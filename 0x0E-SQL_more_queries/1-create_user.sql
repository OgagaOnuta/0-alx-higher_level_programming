-- Creates a MySQL server user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- Grant privileges to user
GRANT ALL ON *.* TO 'user_0d_1'@'localhost'
