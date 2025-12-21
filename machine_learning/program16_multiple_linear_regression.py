# program16_multiple_linear_regression.py

import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset (multiple features)
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([6, 9, 12, 15])

# Model
model = LinearRegression()
model.fit(X, y)

print("Prediction:", model.predict([[5, 6]]))

# Multiple Linear Regression Explanation:

# Multiple Linear Regression is used when the output depends on
# MORE THAN ONE input feature.

# Example:
# House Price depends on:
# - Size
# - Number of rooms
# - Location

# Mathematical form:
# y = b0 + b1*x1 + b2*x2 + ...

# In this program, the model learns how multiple inputs together
# affect the output and predicts a continuous value.

# Used in:
# - House price prediction
# - Sales forecasting
# - Salary prediction using multiple factors