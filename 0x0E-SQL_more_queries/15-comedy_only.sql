-- Lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id=tv_genres.id
JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
WHERE tv_shows.title='Dexter'
ORDER BY tv_genres.name ASC;
