-- 1 INNER JOIN: Orders + Customers
SELECT
    o.order_id,
    c.name AS customer_name,
    o.order_date,
    o.total_amount
FROM orders o
INNER JOIN customers c
    ON o.customer_id = c.customer_id
ORDER BY o.order_date DESC
LIMIT 10;

-- 2 LEFT JOIN: All Customers + Orders (if any)
SELECT
    c.customer_id,
    c.name,
    o.order_id,
    o.total_amount
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
ORDER BY c.customer_id;

-- 3 Total Revenue & Average Order Value
SELECT
    SUM(total_amount) AS total_revenue,
    AVG(total_amount) AS avg_order_value,
    COUNT(order_id)   AS total_orders
FROM orders;

-- 4 Category-wise Sales Using JOIN + GROUP BY
SELECT
    p.category,
    SUM(oi.quantity * oi.price) AS category_sales
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY category_sales DESC;

-- 5 Top Customers (CTE + JOIN)
WITH customer_revenue AS (
    SELECT
        o.customer_id,
        SUM(o.total_amount) AS total_spent
    FROM orders o
    GROUP BY o.customer_id
)
SELECT
    c.name,
    cr.total_spent
FROM customer_revenue cr
JOIN customers c
    ON cr.customer_id = c.customer_id
ORDER BY cr.total_spent DESC
LIMIT 10;
