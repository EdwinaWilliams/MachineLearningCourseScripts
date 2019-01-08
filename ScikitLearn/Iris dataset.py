# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 11:44:45 2019

@author: edwinaw

This script uses the iris dataset that comes with sklearn 
"""
#importing the iris dataset, tree and mathplotlib
from sklearn.datasets import load_iris
from sklearn import tree
from matplotlib import pyplot as plt
import numpy as np

iris = load_iris()

"""
Get to know the data 
"""

# Get the feature (measurement) names 
# What each of the data is for 
print (iris.feature_names)
# Print the names of the differnt type of flowers
print(iris.target_names)
#Getting data for the first index 
print(iris.data[0])


"""
Splitting up the data for test and training

For test 3 datapoints is removed 
(The dataset is split out as follows:
    0 - Setosa
    50- First versicolor
    100 - First virginica
)
"""
#Setting indexes for the first of each flower to use to extract data 
test_idx = [0, 50, 100]

#removing testing data from training, and assigning new data to testing
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

#Getting testing data, and assigning new data to training
test_target = iris.target[ test_idx]
test_data = iris.data[ test_idx]

#Using decision tree to fit the data into a model
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

#Checking the training data
print(test_target)
# Testing predictions
print(clf.predict(test_data))

#visualisation of data 

# The indices of the features that we are plotting
x_index = 0
y_index = 1

# this formatter will label the colorbar with the correct target names
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

plt.figure(figsize=(5, 4))
plt.scatter(iris.data[:, x_index], iris.data[:, y_index], c=iris.target)
plt.colorbar(ticks=[0, 1, 2], format=formatter)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index])

plt.tight_layout()
plt.show()