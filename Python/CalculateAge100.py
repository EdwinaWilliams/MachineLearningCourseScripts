# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 15:02:13 2019

@author: edwinaw
"""
import datetime

print("Welcome, this program calculates in which year your will turn a 100 years old")

name = input("Please enter your name \n")
age = int(input("Please enter your age \n"))

def calAge (age):
    yearToAdd = 100 - age
    yearFunc = datetime.datetime.now().year + yearToAdd 
    
    return yearFunc

year = calAge(age)

print("Hi " + name + " you will be 100 in " + str(year))

