# Cafe Sales Analysis — 2024

A full-year exploratory data analysis of café sales data using Python, Pandas, Matplotlib, and Seaborn.

---

## Project Summary

| Metric | Value |
|--------|-------|
| Total Revenue | £354,047 |
| Total Transactions | 50,311 |
| Average Basket Value | £7.04 |
| Period Covered | January – December 2024 |
| Products Analysed | 15 |

---

## Key Findings

- **Saturday** is the highest-revenue day — 40%+ above a typical Tuesday
- **Lunchtime (12:00–14:00)** is peak trading hour every day of the week
- **Hot Drinks** account for ~35% of total revenue — coffee is the core driver
- **Cappuccino** is the single best-selling product by revenue
- **March and Easter weeks** show consistent revenue spikes — useful for stock planning
- **Cold Drinks** underperform year-round, suggesting a promotional opportunity

---

## Charts

### 1. Monthly Revenue
![Monthly Revenue](charts/01_monthly_revenue.png)

### 2. Revenue by Day of Week
![Day of Week](charts/02_revenue_by_day.png)

### 3. Hourly Footfall Heatmap
![Heatmap](charts/03_hourly_heatmap.png)

### 4. Top Products by Revenue
![Top Products](charts/04_top_products.png)

### 5. Revenue by Category
![Category](charts/05_category_breakdown.png)

### 6. Weekly Revenue Trend
![Weekly Trend](charts/06_weekly_trend.png)

---

## Business Recommendations

| Finding | Recommendation |
|---------|---------------|
| Saturday = highest revenue day | Max staffing on Saturdays; consider extended hours |
| Lunch (12–14:00) is peak hour | Full team + pre-prepared stock before midday daily |
| Hot Drinks = 35% of revenue | Prioritise barista training; upsell coffee with food |
| Cold Drinks underperform | Run a summer iced drink promotion |
| March/Easter spikes | Pre-order extra stock 2 weeks ahead |
| Cappuccino = #1 product | Never let coffee beans run low |

---

## Files

```
cafe-sales-analysis/
├── Cafe_Sales_Analysis.ipynb   # Full analysis notebook
├── cafe_sales_2024.csv         # Dataset (96,676 rows)
├── analysis.py                 # Standalone Python script
├── charts/
│   ├── 01_monthly_revenue.png
│   ├── 02_revenue_by_day.png
│   ├── 03_hourly_heatmap.png
│   ├── 04_top_products.png
│   ├── 05_category_breakdown.png
│   └── 06_weekly_trend.png
└── README.md
```

---

## How to Run

```bash
# Clone the repository
git clone https://github.com/your-username/cafe-sales-analysis.git
cd cafe-sales-analysis

# Install dependencies
pip install pandas matplotlib seaborn jupyter

# Run the notebook
jupyter notebook Cafe_Sales_Analysis.ipynb

# Or run the script directly
python analysis.py
```

---

## Tools & Libraries

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| Pandas | Data loading, cleaning, aggregation |
| Matplotlib | Bar charts, line charts, area charts |
| Seaborn | Heatmap visualisation |
| Jupyter Notebook | Interactive analysis |

---

## About This Project

This analysis was built as part of my Data Analyst portfolio. The dataset is synthetically generated to mirror real café sales patterns, drawing on my 5 years of experience as a Supervisor at Paul Bakery, Regent Street — where I tracked daily sales data, managed stock across 50+ product lines, and produced weekly reports for senior management.

**Author:** Hinal Patel  
**LinkedIn:** [linkedin.com/in/hinalpatel](https://linkedin.com/in/hinalpatel)  
**Email:** Hinalpatel2526@gmail.com
