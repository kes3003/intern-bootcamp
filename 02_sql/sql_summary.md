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
| month  | monthly_sales |
| ------------- | ------------- |
| 2025-06-01 00:00:00+04  | 21469.159999999993  |
| 2025-02-01 00:00:00+04  | 16974.199999999997  |
| 2024-11-01 00:00:00+04  | 14116.000000000002  |
| 2024-12-01 00:00:00+04  | 13510.350000000002  |
| 2025-01-01 00:00:00+04  | 12944.469999999998  |

=> Highest revenue months are June 2025 and February 2025

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
| month  | monthly_sales | monthly_sales |
| ------------- | ------------- | ------------- |
| Tuvalu              | 10105.039999999999 |            5  |
| Antigua and Barbuda |            9266.15 |            5  |
| Taiwan              |            7354.15 |            3  |
| Bangladesh          |            7338.05 |            5  |
| Indonesia           |  6822.570000000001 |            5  |


 => Smaller markets are contributing significant per-order value
