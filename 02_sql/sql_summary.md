# SQL Summary (Week 1)

## Key Insights
1. Database normalized up to **3NF** to remove redundancy.  
2. Added **indexes** on `order_date` and `category` to speed up lookups.  
3. Queries now execute faster on large datasets.

---

## Sample Queries

### 1 Peak Sales Periods

SELECT
    DATE_TRUNC('month', o.order_date) AS month,
    SUM(oi.total_price) AS monthly_sales
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY month
ORDER BY monthly_sales DESC
LIMIT 5;

### 2 Top Revenue-Contributing Customer Segments

SELECT
    c.country,
    SUM(oi.total_price) AS total_revenue,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY c.country
ORDER BY total_revenue DESC
LIMIT 5;
