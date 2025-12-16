# Program 12: K-Means Clustering
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

iris = load_iris()
X = iris.data

kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

print("Cluster labels:", kmeans.labels_[:10])