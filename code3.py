import pandas as pd
import random

products = ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Monitor', 'Keyboard', 'Mouse', 'Smartwatch']
num_records = 10

data = {
    'Product': [random.choice(products) for _ in range(num_records)],
    'Price': [round(random.uniform(100, 5000), 2) for _ in range(num_records)],
    'Quantity': [random.randint(1, 20) for _ in range(num_records)]
}

df = pd.DataFrame(data)
df['Total_Sale'] = df['Price'] * df['Quantity']
total_sales_per_product = df.groupby('Product')['Total_Sale'].sum().sort_values(ascending=False)
best_selling_product = total_sales_per_product.idxmax()
best_selling_value = total_sales_per_product.max()

print("Total sales per product:")
print(total_sales_per_product)
print("\nBest selling product:")
print(f"{best_selling_product} with total sales = {best_selling_value:,.2f} SAR")
