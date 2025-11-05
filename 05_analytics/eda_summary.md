### Exploratory Data Analysis Summary

**Data Overview**

| Dataset | Rows | Columns | Description |
|---------|---------------|--------------|--------------|
| customers_clean.parquet | 50 | 7 | Basic customer demographics and signup info |
| orders_clean.parquet | 100 | 4 | Order-level records with dates and status |
| order_items_clean.parquet | 303 | 4 | Item-level transactions linked to orders |
| products_clean.parquet | 20 | 5 | Product catalog including price & category |
| transactions_clean.parquet | 100 | 5 | Payment details and transaction status 

### Key Visualizations & Insights
**Revenue Trend Over Time**

A steady increase in total daily revenue was observed, with minor fluctuations in early periods — indicating consistent customer engagement and possible recurring purchases.
Insight: Sales momentum is healthy and stable, suggesting effective retention strategies.

**Top Customers by Revenue**

The top 10 customers collectively contribute a significant share (~40%) of total sales.
Insight: A small group of high-value customers drives the majority of revenue — ideal targets for loyalty or premium programs.

**Revenue by Product Category**

Electronics and Clothing dominate total revenue, followed by Home and Sports.
Insight: These categories are core business drivers; promotional focus here yields highest ROI.

**Correlation Heatmap & Price Distribution**

Moderate correlation between price and revenue confirms that both product pricing and quantity purchased affect total sales.
Insight: Electronics show the widest price variance, explaining higher revenue spread.