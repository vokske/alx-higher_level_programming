-- Lists all genres not linked to the show 'Dexter'
-- Each record displays the genre name (tv_genre.name)
-- Results are sorted in ascending order by the genre name
SELECT name FROM tv_genres
WHERE tv_genres.id NOT IN (
	SELECT tv_genres.id FROM tv_genres
	LEFT JOIN tv_show_genres
	ON tv_show_genres.genre_id = tv_genres.id
	LEFT JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_shows.title = 'Dexter')
ORDER BY name;

-- Another potent route to the solution
-- SELECT name FROM tv_genres WHERE id NOT IN (SELECT genre_id FROM tv_show_genres WHERE show_id = 8) ORDER BY name;

