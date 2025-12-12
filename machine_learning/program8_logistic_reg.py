# Program 8: Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, (iris.target == 0)  # Binary: Setosa or not

model = LogisticRegression(max_iter=200)
model.fit(X, y)

print("Prediction:", model.predict([X[0]]))
