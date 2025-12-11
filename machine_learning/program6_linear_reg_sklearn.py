# Program 7: Linear Regression with sklearn
from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([[1],[2],[3],[4],[5]])
y = np.array([1,2,3,4,5])

model = LinearRegression()
model.fit(x, y)

print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)
print("Prediction for 6:", model.predict([[6]]))
