# Write your MySQL query statement below
WITH t AS 
(
    SELECT e.id, e.name as 'Employee', d.name as 'Department', e.salary AS Salary
    FROM Employee e
    JOIN Department d
    ON e.departmentId = d.id
)

SELECT T1.Department, T1.Employee, T1.Salary from 
(
SELECT t.*,
dense_rank() OVER(PARTITION BY t.Department ORDER BY Salary DESC) AS rn
FROM t ) T1
WHERE T1.rn <= 3
ORDER BY T1.Salary DESC