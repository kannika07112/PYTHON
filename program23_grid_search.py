# program23_grid_search.py

from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

X, y = load_iris(return_X_y=True)

params = {
    "C": [0.1, 1, 10],
    "kernel": ["linear", "rbf"]
}

grid = GridSearchCV(SVC(), params)
grid.fit(X, y)

print("Best Parameters:", grid.best_params_)


# GridSearchCV Explanation:

# GridSearchCV is used to find the best combination
# of hyperparameters for a machine learning model.

# It performs:
# - Cross-validation
# - Parameter optimization

# This improves model accuracy and prevents overfitting.

# Used in:
# - Model optimization
# - ML competitions
# - Production-ready ML systems