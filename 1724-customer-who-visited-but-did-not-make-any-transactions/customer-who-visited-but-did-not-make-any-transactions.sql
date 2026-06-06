# Write your MySQL query statement below
-- SELECT 
-- FROM Visits v 
-- JOIN Transaction t USING (visit_id)


SELECT DISTINCT customer_id, COUNT(visit_id) as  count_no_trans
FROM Visits WHERE  visit_id NOT IN 
( 
SELECT DISTINCT visit_id FROM Transactions
)
group by customer_id