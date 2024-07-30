-- List all California cities found in a DB in my MYSQL server
SELECT id, name
FROM cities
WHERE id = (SELECT id FROM states WHERE name='California');

