# Program 4: Basic Matplotlib plots
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, label="Line Plot")
plt.scatter(x, y, color="red", label="Scatter")
plt.legend()
plt.show()
