# import class...
import numpy as np
from sklearn.linear_model import LinearRegression

# define input/indipendant (X) and output/dependant (y)
X = [10, 15, 25, 35, 45, 55]
y = [5, 20, 15, 35, 22, 39]

X2 = np.array([5, 15, 25, 35, 45, 55]).reshape(-1, 1)
y2 = np.array([5, 20, 14, 32, 22, 38])

print("X2: ", X2)
print("y2: ", y2)

# Calculate the best formula  f(x) = b0 + b1X
# fit calculate the best b0 and b1
"""
model = LinearRegression()
model.fit(X2, y2)
the same of row just below...
"""
model = LinearRegression().fit(X2, y2)

# Show how model fit...
# R2 --> means coefficient of determination. R2 = 1 best fit; R2 < 1 progressive bad fit
r_sq = model.score(X2, y2)
print('coefficient of determination:', r_sq) # model fit well (near 1)

# b0 o intercept on y axis...
b0 = model.intercept_
print('intercept:', b0)

# b1 (in f(x) = b0 + b1X) - Coefficient...
b1 = model.coef_
print("Coefficient x: (or slope)",b1)

"""
The value b0 = 5.63 (approximately) illustrates that your model predicts the response 5.63 when 𝑥 is zero. 
The value b1 = 0.54 means that the predicted response rises by 0.54 when X is increased by one.
"""

# Predict...
# Its the same as apply f(x) = b0 + b1X i.e. model.predict_ + model-coef_ * X
y_pred = model.predict(X2)
print('predicted response:', y_pred, sep='\n')


