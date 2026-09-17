import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales_data.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order_ID"].nunique()
aov = total_sales / total_orders
profit_margin = total_profit / total_sales * 100

print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Quantity:", total_quantity)
print("Total Orders:", total_orders)
print("Average Order Value:", round(aov, 2))
print("Profit Margin:", round(profit_margin, 2), "%")

monthly = df.groupby(df["Order_Date"].dt.to_period("M")).agg(
    Sales=("Sales","sum"), Profit=("Profit","sum")
).reset_index()
monthly["Order_Date"] = monthly["Order_Date"].astype(str)

category = df.groupby("Category").agg(
    Sales=("Sales","sum"), Profit=("Profit","sum"), Quantity=("Quantity","sum")
).sort_values("Sales", ascending=False)

region = df.groupby("Region").agg(
    Sales=("Sales","sum"), Profit=("Profit","sum")
).sort_values("Profit", ascending=False)

top_products = df.groupby("Product").agg(
    Sales=("Sales","sum"), Profit=("Profit","sum"), Quantity=("Quantity","sum")
).sort_values("Sales", ascending=False).head(10)

print("\nCategory Performance:\n", category)
print("\nRegion Performance:\n", region)
print("\nTop Products:\n", top_products)

plt.figure(figsize=(10,5))
plt.plot(monthly["Order_Date"], monthly["Sales"], marker="o", label="Sales")
plt.plot(monthly["Order_Date"], monthly["Profit"], marker="o", label="Profit")
plt.xticks(rotation=45)
plt.title("Monthly Sales & Profit")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.tight_layout()
plt.show()

category["Sales"].plot(kind="bar", figsize=(8,5), title="Sales by Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

region["Profit"].plot(kind="bar", figsize=(8,5), title="Profit by Region")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

top_products["Sales"].plot(kind="bar", figsize=(9,5), title="Top Products by Sales")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
