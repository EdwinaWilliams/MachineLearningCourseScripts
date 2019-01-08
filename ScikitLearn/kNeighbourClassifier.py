# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:54:50 2019

@author: edwinaw
"""

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

print ("X_Train " ) 
print ( X_train) 
print ("**************************************************")
print ("X_Test = " ) 
print (+ X_Test) 
print ("**************************************************")
print ("y_train = " ) 
print ( y_train) 
print ("**************************************************")
print ("y_test = " ) 
print (y_test) 

#using the KNeighborsClassifier ==> called a pipeline 
from sklearn.neighbors import KNeighborsClassifier
my_classifier = KNeighborsClassifier()

my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_Test)
#Checking models accuracy 
from sklearn.metrics import accuracy_score
print( accuracy_score(y_test, predictions))