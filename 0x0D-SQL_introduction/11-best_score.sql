-- Lists all records that meet a condition
-- in a table of a database in MySQL server
SELECT score, name
FROM second_table
WHERE (score >= 10)
ORDER BY score DESC;
