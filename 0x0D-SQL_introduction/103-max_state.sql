-- Import a table dump to a databas on my MYSQL server
-- Display the max temperature of each state (ordered by state name)
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;

