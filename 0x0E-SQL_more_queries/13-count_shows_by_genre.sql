-- this query will show number of tv shows related to the genres
SELECT tv_genres.name AS 'genre', COUNT(tv_genres.id)
AS 'number_of_shows'
FROM tv_genres
RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id, tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
