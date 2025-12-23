# program17_multiclass_logistic_regression.py

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))

# Multiclass Logistic Regression Explanation:

# Logistic Regression is used for classification problems.
# Multiclass Logistic Regression is used when there are
# MORE THAN TWO classes.

# Example:
# - Flower classification (Setosa, Versicolor, Virginica)

# The model predicts probabilities for each class and
# selects the class with the highest probability.

# Used in:
# - Image classification
# - Medical diagnosis with multiple conditions
# - Text classification