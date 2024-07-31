-- Import a database dump
-- From the tables in the database,
-- list all shows that have at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres, tv_shows
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;

