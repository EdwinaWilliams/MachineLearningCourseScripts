# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:37:46 2019

@author: egwil
"""

""""
importing libraries
    numpy
    pandas
    train_test_split
    prepocessing
"""
import numpy as np
import pandas as pd
#importing test/train split function --> will help in choosing models
from sklearn.model_selection import train_test_split
#contains utilities for scaling, transforming, and wrangling data
from sklearn import preprocessing
#importing model families **what are these families and what is the models**
from sklearn.ensemble import RandomForestRegressor
# importing the tools to help us perform cross-validation
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
#metrics we can use to evaluate our model performance 
from sklearn.metrics import mean_squared_error, r2_score
# import a way to persist our model for future use
from sklearn.externals import joblib

"""
Importing data from remote location
and printing first 5 rows
"""

dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url, sep=';')
#first 5 rows
#print (data.head())
#data structure
#print(data.shape)
#summary statistics
#print(data.describe())

"""
Data splitting 
Splitting target (Quality of data) from the training data 
"""
#Quality measurement of data 
y = data.quality 
X =  data.drop('quality', axis=1)
#test set is 2% of data, random state is used to ensure that we are able to reproduce results 
#stratify ensures that the training data is the same as testing data
X_train, X_test, y_train , y_test = train_test_split(X, y, test_size =0.2, random_state=123,stratify=y)


"""
Data standardization
Used transformer API to fit the data 
see webpage for more info why this is being used
https://elitedatascience.com/python-machine-learning-tutorial-scikit-learn
Also more info on general standardization code
"""
	
scaler = preprocessing.StandardScaler().fit(X_train)
#testing scalar 

X_train_scaled = scaler.transform(X_train)
print (X_train_scaled.mean(axis=0))
print (X_train_scaled.std(axis=0))