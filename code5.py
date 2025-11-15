
# Question:
# -The code below is used to group IoT devices into 2 clusters based on their temperature and humidity readings using K-Means clustering. Use the following data:
# Temperature (°C): [25, 30, 35, 28, 32]  
# Humidity (%): [60, 55, 70, 65, 50]

# -What is the expected output from running the code below?
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
# Data for clustering
temperature = [25, 30, 35, 28, 32]
humidity = [60, 55, 70, 65, 50]
# Combine data into a 2D array
data = np.array(list(zip(temperature, humidity)))
# Apply K-Means Clustering
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(data)
# Plot the clusters
plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_, cmap='viridis', label="Data Points")
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='red', marker='x', label="Centroids")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.title("K-Means Clustering of IoT Data")
plt.legend()
plt.show()