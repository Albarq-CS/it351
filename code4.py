import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate random records
users = np.random.randint(1, 11, 50)
pages = np.random.choice(['Home', 'Profile', 'Products', 'Contact', 'About'], 50)
devices = np.random.choice(['Mobile', 'Desktop', 'Tablet'], 50)
durations = np.random.randint(10, 600, 50)

data = pd.DataFrame({
    'UserID': users,
    'Page': pages,
    'Device': devices,
    'Duration': durations
})

# Step 2: Most visited page
page_visits = data['Page'].value_counts()
most_visited_page = page_visits.idxmax()

# Step 3: Most used device
device_usage = data['Device'].value_counts()
most_used_device = device_usage.idxmax()

# Step 4: Average session duration per user
avg_duration_per_user = data.groupby('UserID')['Duration'].mean()

# Display results
print("=== Website Analytics Results ===")
print("\nPage Visit Count:")
print(page_visits)

print("\nMost Visited Page:", most_visited_page)

print("\nDevice Usage Count:")
print(device_usage)

print("\nMost Used Device:", most_used_device)

print("\nAverage Session Duration Per User:")
print(avg_duration_per_user)

# Step 5: Visualization
plt.figure(figsize=(12,5))

# Bar Chart: Page Visits
plt.subplot(1,2,1)
page_visits.plot(kind='bar')
plt.title('Page Visits')
plt.xlabel('Page')
plt.ylabel('Visits')

# Pie Chart: Device Usage
plt.subplot(1,2,2)
device_usage.plot(kind='pie', autopct='%1.1f%%')
plt.title('Device Usage')
plt.ylabel('')

plt.tight_layout()
plt.show()
