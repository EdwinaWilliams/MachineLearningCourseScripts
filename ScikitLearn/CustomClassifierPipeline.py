# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:54:50 2019

@author: edwinaw
"""
"""
Iris dataset is defined as a cube because of its number of dimensions
Defining the KN class that will be used to classify the data 
K is the number of neighbors that should be considered in making our prediction (majority class)
    Finding the nearest neighbor:Straight line distance --> Euclidean distance
    Formula: d(a,b)= sqrt((x2-x1)**2 + (y2-y1)**2) (triangle --> Pythorean theory)
    Note: with the Euclidean distance you can have n number of terms 
"""

#Getting the distance function fro the spatial library (Euclidean distance )
#from scrip.spatial import distance 
#from .script import distance 
import math

#function: will calculate the distance 
def euc(a,b):
    return distance.euclidean(a,b)

class BasicKNN():
    #adding two functions: Fit (train) and predict
    
    #input is the training data features and target values 
    def fit(self, X_train, y_train): 
        #feeding the model the data 
        self.X_train = X_train
        self.y_train = y_train
        
    
    #input is the testing datase 
    def predict(self, X_test):
        #creating a list that will store the predictions
        predictions = []
        """
        this loop will iterate over each datapoint in the test dataset and assign a prediction label to it
        iteration in this method makes the model slower
        """
        for row in X_test: 
            #find the closest point in the test set (neighbor K=1)
            label = self.closest(row)
            predictions.apped(label)
        return predictions
            
    #memorise how close the element is to the training example 
    def closest(self, row):
        best_dist = euc(row, self.X_train[0])
        best_index = 0 
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
            return self.y_train[best_index]
#importing the iris dataset     
from sklearn import datasets
iris = datasets.load_iris()


#function F(x))= y
X =  iris.data 
y = iris.target 

#splitting dataset into random training and test set 
from sklearn.model_selection import train_test_split
"""
 Sample size set to half the data set
 Splitting dataset into train and test 
 
 #Features
 X_Train ==> training dataset (50%)
 X_Test ==> testing dataset (50%)
 #Values
 y_train ==> testing target values (50%)
 y_test ==>testing target values (50%)
"""
X_train, X_Test, y_train, y_test = train_test_split(X, y, test_size = .5)


my_classifier = KNeighborsClassifier()

my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_Test)
#Checking models accuracy 
from sklearn.metrics import accuracy_score
print( accuracy_score(y_test, predictions))