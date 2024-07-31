-- List all shows and all genres linked to that show
-- If a show doesn't have a genre, 'NULL' is displayed in the genre column
-- Each record displays tv_shows.title - tv_genres.name
-- Results are sorted in ascending order by the show title and genre name
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;

