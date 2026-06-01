# Write your MySQL query statement below
SELECT DISTINCT a.num AS ConsecutiveNums
FROM Logs a
JOIN Logs b 
ON a.num = b.num AND a.id = b.id+1
JOIN Logs c
ON a.num = c.num AND a.id = c.id+2