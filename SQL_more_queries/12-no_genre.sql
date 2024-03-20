#!/usr/bin/env bash
-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT genres.name AS genre,
       COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
JOIN genres ON tv_show_genres.genre_id = genres.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
