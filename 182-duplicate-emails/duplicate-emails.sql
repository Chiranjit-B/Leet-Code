with cte as 
(
    SELECT email, count(p.email) as em
    From Person p
    GROUP BY email 
)
SELECT cte.email AS Email from cte
WHERE cte.em > 1 