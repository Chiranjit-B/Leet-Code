-- SELECT MAX(salary) AS SecondHighestSalary FROM Employee
-- WHERE SALARY < (select MAX(SALARY) FROM Employee)
-- ORDER BY SecondHighestSalary desc limit 1

SELECT MAX(Salary) As SecondHighestSalary
FROM Employee
WHERE Salary NOT IN (SELECT MAX(salary) FROM Employee)
