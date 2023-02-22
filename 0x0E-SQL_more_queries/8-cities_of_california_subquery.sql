-- Lists all detail found in a database that matches a certain condition
SELECT id, name
FROM cities
WHERE (SELECT id FROM states
      WHERE (name = 'California'))
ORDER BY cities.id;
