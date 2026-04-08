-- Write your query below
WITH CTE AS
(
    SELECT * FROM customers 
    WHERE year = 2020 and revenue > 0
)
SELECT distinct(customer_id) FROM CTE ; 