# Write your MySQL query statement below
with cte as 
(
SELECT managerId, count(managerId) as cnt
FROM Employee
GROUP BY managerId
HAVING cnt >= 5
)
select name from Employee 
WHERE id IN  (select managerId FROM CTE)
