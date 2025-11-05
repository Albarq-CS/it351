import pandas as pd
import random
import matplotlib.pyplot as plt

# 1. Generate random sales data
products = ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Monitor', 'Keyboard', 'Mouse', 'Smartwatch']
num_records = 1000  # Number of sales records

data = {
    'Product': [random.choice(products) for _ in range(num_records)],
    'Price': [round(random.uniform(100, 5000), 2) for _ in range(num_records)],
    'Quantity': [random.randint(1, 20) for _ in range(num_records)]
}

df = pd.DataFrame(data)

# 2. Calculate total sales for each transaction
df['Total_Sale'] = df['Price'] * df['Quantity']

# 3. Calculate total sales per product
total_sales_per_product = df.groupby('Product')['Total_Sale'].sum().sort_values(ascending=False)

# 4. Identify the best-selling product
best_product = total_sales_per_product.idxmax()
best_value = total_sales_per_product.max()

# 5. Display the results
print("Total sales per product:")
print(total_sales_per_product)
print(f"\nBest selling product: {best_product} with total sales = {best_value:,.2f} SAR")

# 6. Plot bar chart
plt.figure(figsize=(8,5))
plt.bar(total_sales_per_product.index, total_sales_per_product.values)
plt.title('Total Sales per Product')
plt.xlabel('Product')
plt.ylabel('Total Sales (SAR)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
