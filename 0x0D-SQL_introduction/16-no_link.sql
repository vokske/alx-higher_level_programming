-- Lists all records of the table where name is NULL
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;

