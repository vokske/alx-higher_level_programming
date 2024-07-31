-- Lists all genres from hbtn_0d_tvshows database
-- Displays the number of shows linked to each genre
-- Each record displays genre - number_of_shows
-- Results are sorted in descending order by number_of_shows
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres
JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;

