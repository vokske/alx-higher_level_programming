-- List all shows that are not of genre 'Comedy'
-- Each record displays tv_shows.title
-- Results are sorted in ascending order by show title
-- Query consists of a maximum two SELECT statements
SELECT title FROM tv_shows
WHERE id NOT IN (
	SELECT tv_shows.id FROM tv_shows
	LEFT JOIN tv_show_genres
	ON tv_show_genres.show_id = tv_shows.id
	LEFT JOIN tv_genres
	ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_genres.name = 'Comedy')
ORDER BY title;

