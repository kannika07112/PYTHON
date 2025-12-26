# program20_kmeans_elbow.py

import numpy as np
from sklearn.cluster import KMeans

X = np.array([[1,2],[1,4],[5,8],[6,9],[1,0],[9,8]])

wcss = []
for k in range(1, 6):
    model = KMeans(n_clusters=k)
    model.fit(X)
    wcss.append(model.inertia_)

print("WCSS values:", wcss)

# K-Means Clustering with Elbow Method Explanation:

# K-Means is an unsupervised learning algorithm used
# to group similar data points into clusters.

# The Elbow Method helps in finding the optimal
# number of clusters (K) by analyzing WCSS values.
# WCSS-Within-Cluster Sum of Sqaures- 
# Measures how tightly data points are grouped inside each other

# Used in:
# - Customer segmentation
# - Market analysis
# - Image compression
# - Pattern recognition