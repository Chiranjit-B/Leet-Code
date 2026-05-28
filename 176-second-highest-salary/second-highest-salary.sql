SELECT MAX(salary) AS SecondHighestSalary FROM Employee
WHERE SALARY < (select MAX(SALARY) FROM Employee)
ORDER BY SecondHighestSalary desc limit 1
