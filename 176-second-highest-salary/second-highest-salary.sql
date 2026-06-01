# Write your MySQL query statement below
SELECT MAX(salary) AS SecondHighestSalary FROM Employee
WHERE salary < (Select MAX(salary) FROM Employee)

-- ORDER BY Salary DESC
-- LIMIT 1