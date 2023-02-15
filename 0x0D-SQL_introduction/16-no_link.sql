-- Lists all records of a table of a database in MySQL server
SELECT score, name
FROM second_table
ORDER BY score DESC
WHERE name =
      (SELECT name
      FROM second_table);
