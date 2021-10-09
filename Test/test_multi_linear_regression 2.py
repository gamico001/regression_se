"""
l'input, in questo caso, consiste in un array di valori. Quindi X è un array a più dimensioni, come nel caso,
ad esempio, di determinare lo stipendio atteso (y) in base a età e area geografica (i due valori X).
Dovrebbe essere la risoluzione di f(x) = b0 + b1x1 + b2x2
"""
import numpy as np
from sklearn.linear_model import LinearRegression

x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]] # 2 input --> v1 & x2
y = [4, 5, 20, 14, 32, 22, 38, 43] # 1 output --> y
x, y = np.array(x), np.array(y) # transform in array!

print("x:", x)
print("y:", y)

# fit model
model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)

print('intercept:', model.intercept_)
print('slope:', model.coef_) # 2 coefficienti

# predict
y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')
# similar to: y_pred = model.intercept_ + np.sum(model.coef_ * x, axis=1)

# You can apply this model to new data as well:
x_new = np.arange(10).reshape((-1, 2))
print(x_new)

y_new = model.predict(x_new)
print(y_new)


