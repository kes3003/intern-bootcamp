-- 1 View all customers (first 10)
SELECT * FROM customers
LIMIT 10;

-- 2 Customers from a specific city
SELECT name, city, country
FROM customers
WHERE city = 'Dubai';

-- 3 Top 10 newest customers by created date
SELECT name, email, created_at
FROM customers
ORDER BY created_at DESC
LIMIT 10;

-- 4 List all products sorted by price
SELECT product_id, product_name, price
FROM products
ORDER BY price DESC;

-- 5 Count orders per day
SELECT order_date, COUNT(*) AS daily_orders
FROM orders
GROUP BY order_date
ORDER BY order_date DESC;
