# Sales & Revenue Analysis Dashboard

A portfolio-ready Sales & Revenue Analysis project using Python, Pandas, Matplotlib, SQL concepts, and Power BI.

## Objective
Analyze sales performance, revenue, profit, products, categories, regions, customer segments, discounts, and payment modes.

## Dataset
The included dataset is **synthetic** and created for learning/portfolio purposes.

Columns:
- Order_ID
- Order_Date
- Product
- Category
- Region
- Sales
- Quantity
- Discount
- Profit
- Customer_Segment
- Payment_Mode

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- Power BI
- SQL

## Project Structure
```text
sales-revenue-analysis-dashboard/
├── data/
│   └── sales_data.csv
├── python/
│   └── sales_analysis.py
├── powerbi/
│   ├── DAX_Measures.md
│   └── Dashboard_Layout.md
├── requirements.txt
├── .gitignore
└── README.md
```

## KPIs
- Total Sales
- Total Profit
- Profit Margin
- Total Orders
- Average Order Value
- Total Quantity

## Python
Install dependencies:
```bash
pip install -r requirements.txt
```

Run:
```bash
python python/sales_analysis.py
```

## Power BI
Import `data/sales_data.csv` into Power BI Desktop and use the DAX measures and dashboard layout in the `powerbi` folder.

## Dashboard
Recommended visuals include monthly sales/profit trends, sales by category, profit by region, top products, customer segments, and payment modes.

## Conclusion
This project demonstrates an end-to-end analytics workflow: data preparation, KPI calculation, exploratory analysis, visualization, and dashboard design. Because the dataset is synthetic, the findings should be treated as portfolio demonstrations rather than real business results.
