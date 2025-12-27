# program21_pca.py

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

X, y = load_iris(return_X_y=True)

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print("Original shape:", X.shape)
print("Reduced shape:", X_reduced.shape)


# Principal Component Analysis (PCA) Explanation:

# PCA is a dimensionality reduction technique.

# It reduces the number of input features while
# preserving maximum important information (variance).

# Benefits:
# - Faster model training
# - Reduced storage
# - Better visualization

# Used in:
# - Image processing
# - Data compression
# - High-dimensional data analysis