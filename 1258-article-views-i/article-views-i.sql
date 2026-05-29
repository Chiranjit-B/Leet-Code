# Write your MySQL query statement below
SELECT DISTINCT(a.author_id)  AS id FROM 
Views a 
JOIN Views b 
ON a.article_id = b.article_id  AND a.author_id = b.viewer_id
ORDER BY id ASC
