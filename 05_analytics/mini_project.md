### Project Question

“Which product categories contribute most to repeat purchases?”

***Implementation Highlights***

- SQL Query - PostgreSQL - Grouped orders by customer_id, counted orders, flagged is_repeat = True/False
- Data Merge - Pandas + PyMongo - Joined orders, order_items, and products for category mapping
- Aggregation - Pandas groupby - Calculated total revenue & average order value per category for repeat buyers
- Visualization - Seaborn / Matplotlib - Bar charts showing category performance by repeat frequency

***Key Findings***

1. Electronics & Clothing lead repeat sales
   -  These two categories account for ≈ 65 % of all repeat purchases.
   -  Customers who initially buy gadgets or apparel tend to return for upgrades or new styles.

2. Home & Sports categories drive one-time orders
   -  Lower repeat rates suggest these are occasion-based or seasonal purchases.

3. Repeat customers generate 2.3× higher average revenue
   -  Retention initiatives in top categories can amplify ROI significantly.

***Business Implications***

- Focus marketing on Electronics & Clothing repeat buyers through bundles and loyalty discounts.
- Re-engage one-time customers from Home/Sports segments via seasonal campaigns.
- Use repeat buyer signals to feed future recommendation models or churn analysis.