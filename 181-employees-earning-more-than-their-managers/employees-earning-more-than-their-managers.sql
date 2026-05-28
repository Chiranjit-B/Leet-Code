# Write your MySQL query statement below
WITH cte AS
(
    SELECT e.id, e.name, e.salary as emp_sal, m.salary as man_sal FROM Employee e
    JOIN Employee m 
    ON e.managerID = m.id

)

SELECT cte.name as Employee FROM cte
WHERE 
cte.emp_sal > cte.man_sal 