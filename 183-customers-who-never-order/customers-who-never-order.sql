# Write your MySQL query statement below
WITH CTE AS 
(

    SELECT c.id, c.name, o.customerId
    FROM Customers c
    LEFT JOIN Orders o 
    ON c.id = o.customerID
    
)
SELECT name as Customers FROM cte
WHERE cte.customerId is NULL 
    
