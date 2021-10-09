"""
Regression test
"""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

"""
sklean.PolynomialFeatures: degree, input=1
- degree = 2 --> f(x) = b0 + b1x1 + b2x^2
- degree = 3 --> f(x) = b0 + b1x1 + b2x^2 + b3x^3
"""

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([15, 11, 2, 8, 25, 32])

print("x:", x)

transformer = PolynomialFeatures(degree=4, include_bias=False)

transformer.fit(x)
x_ = transformer.transform(x)
print("x_:", x_)
"""


# ---------------------
#  𝑓(𝑥₁, 𝑥₂) = 𝑏₀ + 𝑏₁𝑥₁ + 𝑏₂𝑥₂ + 𝑏₃𝑥₁² + 𝑏₄𝑥₁𝑥₂ + 𝑏₅𝑥₂².
# ---------------------
# Step 2a: Provide data
x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]
x, y = np.array(x), np.array(y)
print("x:", x)


# Step 2b: Transform input data
x_ = PolynomialFeatures(degree=2, include_bias=False).fit_transform(x)
print("x_:", x_)
"""