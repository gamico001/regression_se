"""
Decision tree test
"""

# Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier  # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split  # Import train_test_split function
from sklearn import metrics  # Import scikit-learn metrics module for accuracy calculation

# Date...
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
# load dataset
pima = pd.read_csv(
    "/Users/giorgio/Library/Mobile Documents/com~apple~CloudDocs/WORKSPACES/Pycharm/superenalotto/Data/diabetes.csv",
    header=1, names=col_names)

pima.head()

print("pima:", pima)

"""
Feature Selection
Here, you need to divide given columns into two types of variables dependent(or target variable, IL RISULTATO) 
and independent variable(or feature variables GLI INDICATORI CHE HANNO GENERATO IL RISULTATO).
"""
# split dataset in features and target variable
feature_cols = ['pregnant', 'insulin', 'bmi', 'age', 'glucose', 'bp', 'pedigree']  # gli Indicatori,
X = pima[feature_cols]  # Features  gli Indicatori
y = pima.label  # Target variable. Label è il risultato, quì è 0=no 1=si

"""
To understand model performance, dividing the dataset into a training set and a test set is a good strategy.
Let's split the dataset by using function train_test_split(). You need to pass 3 parameters features, 
target, and test_set size.
"""
# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)  # 70% training and 30% test

"""
Let's create a Decision Tree Model using Scikit-learn.
"""
# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)

"""
Let's estimate, how accurately the classifier or model can predict the type of cultivars.
Accuracy can be computed by comparing actual test set values and predicted values.
"""
# Model Accuracy, how often is the classifier correct?
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
