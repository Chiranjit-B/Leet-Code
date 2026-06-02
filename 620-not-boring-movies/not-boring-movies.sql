# Write your MySQL query statement below
SELECT *
FROM Cinema 
WHERE description != 'Boring' AND id%2 != 0
ORDER BY rating DESC