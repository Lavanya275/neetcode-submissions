-- Write your query below
select name from customers c
LEFT JOIN orders o
ON o.customer_id=c.id
where o.id is NULL;