# Week 1 – SQL Joins, Grouping & Aggregation

## Learning Focus
- JOIN operations: **INNER**, **LEFT**, **RIGHT** and how they differ  
- Using **GROUP BY** and **HAVING** for aggregations  
- Writing **CTEs (WITH clauses)** and subqueries  
- Summarizing data for business reporting  

---

## Tasks
1. Combine data across `orders`, `customers`, and `products`.  
2. Compute metrics such as:  
   - Total revenue  
   - Average order value  
   - Sales by product category  
3. Use **CTEs** for top-performing customers & categories.  
4. Add clear comments explaining each query block.

---

## Deliverables
| File | Description |
|-------|--------------|
| `02_joins_groupby.sql` | SQL file with all join, group-by, and CTE queries |
| `joins_groupby_summary.md` | Summary with small output tables or screenshots |

---


Summary example screenshots:

1. INNER JOIN: Orders + Customers

| order_id  | customer_name   | order_date  | status |
|-------|--------------| --------------| --------------|
|  48 | Andrea Lewis    | 2025-10-28 | Shipped |
| 51 | Anthony Jenkins | 2025-10-26 | Cancelled |
| 96 | Sarah Garrett   | 2025-10-01 | Cancelled |
| 85 | Patrick Gates   | 2025-09-30 | Delivered |
| 43 | Isaac Espinoza  | 2025-09-24 | Pending |
| 46 | Larry Sandoval  | 2025-09-22 | Delivered |
| 62 | Kimberly Smith  | 2025-09-12 | Cancelled |
| 27 | Zachary Holmes  | 2025-09-11 | Delivered |
| 18 | Benjamin Park   | 2025-09-08 | Shipped |
| 19 | Justin Mckenzie | 2025-09-07 | Shipped |


2. Total Revenue & Average Order Value

| total_revenue | avg_order_value | total_orders |
|-------|--------------| --------------|
|  132871.91000000003 | 432.80752442996754 |          100 |