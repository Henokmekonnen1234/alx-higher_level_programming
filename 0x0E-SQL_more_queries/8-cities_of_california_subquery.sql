-- this query will show only cities of claifornia state
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
AND states.name = "California"
ORDER BY cities.id;
