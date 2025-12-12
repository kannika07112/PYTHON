# Program 6: Linear Regression using formula
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

m = ((x - x.mean())*(y - y.mean())).sum() / ((x - x.mean())**2).sum()
c = y.mean() - m * x.mean()

print("Slope (m):", m, "Intercept (c):", c)
