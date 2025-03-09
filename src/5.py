import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv('scientific_data.csv')

# Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Cluster the data using KMeans
kmeans = KMeans(n_clusters=5, random_state=0).fit(scaled_data)

# Get the cluster assignments
labels = kmeans.labels_

# Print the clusters
print(labels)