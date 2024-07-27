-- Imports table dump to database
-- Displays the top three cities by average temp during July & August
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month IN (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;

