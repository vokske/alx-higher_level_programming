-- Import the database hbtn_0d_tvshows_rate dump to my MySQL server
-- List all shows from hbtn_0d_tvshows_rate by their rating
-- Each record should display tv_shows.title - rating sum
-- Results are sorted in descending order by the rating
SELECT title, SUM(tv_show_ratings.rate) AS 'rating sum' FROM tv_shows
JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY SUM(tv_show_ratings.rate) DESC;

