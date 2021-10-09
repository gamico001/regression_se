"""
Implementing polynomial regression with scikit-learn is very similar to linear regression.
There is only one extra step: you need to transform the array of inputs to include non-linear terms such as 𝑥².
"""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# data
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1)) # reshape to make e bi-dimensional array
y = np.array([15, 11, 2, 8, 25, 32])
print("x:", x)
print("y:", y)

# Transform input data...
transformer = PolynomialFeatures(degree=2, include_bias=False)
transformer.fit(x)
x_ = transformer.transform(x)
# or siply: x_ = PolynomialFeatures(degree=2, include_bias=False).fit_transform(x)
print("x_:", x_)
# The modified input array contains two columns: one with the original inputs and the other with their squares.

# model
model = LinearRegression().fit(x_, y)

# Result...
r_sq = model.score(x_, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('coefficients:', model.coef_)

"""
The first column of x_ contains ones, the second has the values of x, while the third holds the squares of x.

Alternativa:
you can provide fit_intercept=False
model = LinearRegression(fit_intercept=False).fit(x_, y)
r_sq = model.score(x_, y)
print('intercept:', model.intercept_)
print('coefficients:', model.coef_)
"""

# predict...
y_pred = model.predict(x_)
print('predicted response:', y_pred, sep='\n')
