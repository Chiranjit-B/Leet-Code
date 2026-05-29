SELECT d.name AS 'Department', e.name AS 'Employee', e.salary as Salary
FROM Employee e
JOIN Department d
On e.departmentId = d.id
WHERE (e.departmentId, Salary) IN

(SELECT departmentId, MAX(salary) 
FROM Employee 
GROUP BY departmentId)