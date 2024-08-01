-- Lists all genres not linked to the show 'Dexter'
-- Each record displays the genre name (tv_genre.name)
-- Results are sorted in ascending order by the genre name
SELECT name FROM tv_genres WHERE id NOT IN (SELECT genre_id FROM tv_show_genres WHERE show_id = 8) ORDER BY name;

