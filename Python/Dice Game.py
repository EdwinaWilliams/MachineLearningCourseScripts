# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 22:18:01 2019

@author: edwinaw
"""
import random 

#variable declaration
min = 1 
max = 6

roll = "yes"



while roll == "yes" or roll == "y": 
    print("Rolling the dices...")
    dice = random.randint(min, max)
    #Printing the random number generated
    print("You rolled.. " + str(dice))
    #Asking the user if they want to roll the dice again 
    roll = input("Do you want to roll the dice again? \n")    
        








