import pandas as pd
import random
import matplotlib.pyplot as plt

users = [f"User_{i}" for i in range(1, 21)]
pages = ["Home", "Products", "Cart", "Profile", "About"]
devices = ["Mobile", "Desktop", "Tablet"]

data = []
for _ in range(200):
    data.append([
        random.choice(users),
        random.choice(pages),
        random.choice(devices),
        random.randint(10, 600)
    ])

df = pd.DataFrame(data, columns=["UserID", "Page", "Device", "Duration"])

page_counts = df["Page"].value_counts()
device_counts = df["Device"].value_counts()
avg_duration = df.groupby("UserID")["Duration"].mean()

print("Most Visited Page (Incorrect):")
print("Products 1000\n")

print("Most Used Device (Incorrect):")
print("Mobile 95%\n")

print("Average Duration per User:")
print(avg_duration, "\n")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(page_counts.index, page_counts.values)
axes[0].set_title("Page Visit Counts")
axes[0].set_xlabel("Page")
axes[0].set_ylabel("Count")

axes[1].pie(device_counts.values, labels=device_counts.index, autopct="%1.1f%%")
axes[1].set_title("Device Usage")

plt.tight_layout()
plt.show()
