-- Write your query below
Select customer_id, customer_name from customers 
where customer_id IN (Select customer_id from orders where product_name='A')
AND customer_id IN (Select customer_id from orders where product_name='B')
AND customer_id Not IN (Select customer_id from orders where product_name='C')
order by customer_name;