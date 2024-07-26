-- List the number if records with same score in a table
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;

