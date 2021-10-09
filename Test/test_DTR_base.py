from sklearn.tree import DecisionTreeRegressor

X = [[1][2][3][4][5]]
y = [10, 20, 23, 25, 31]

print("X: ", X)
print("y: ", y)

# create a regressor object
reg = DecisionTreeRegressor(random_state=0)

# fit the regressor with X and Y data
reg.fit(X, y)

# predicting a new value

# test the output by changing values, like 3750
# y_pred = reg.predict(4)

# print the predicted price
# print("Predicted price: % d\n" % y_pred)
