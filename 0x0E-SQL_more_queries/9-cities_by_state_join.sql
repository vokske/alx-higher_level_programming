-- Join the `states` and `cities` tables
-- List all cities by their id, name, and state
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id
ORDER BY cities.id;

