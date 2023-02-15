-- Lists the number of same records in a
-- table of a database in MySQL server
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
