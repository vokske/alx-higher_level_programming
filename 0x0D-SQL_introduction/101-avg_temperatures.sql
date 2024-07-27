-- Import a table dump to database
-- Display the average temperature by city ordered by temperature
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp;

