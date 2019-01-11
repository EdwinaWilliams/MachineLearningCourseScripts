# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 22:55:40 2019

@author: edwinaw
"""


#importing of modules
import random 

#variable declaration
runningGuess = 0
maxGuess = 5
min = 1
max = 47
index = random.randint(min, max)


# Importing random word based on random guess  

with open ("HangManWords.txt") as words: 
    word = words.read().split('\n') [index]


#functions 
    
#def masking(randword):
wordlen = len(word)
   
if wordlen < 4:
   maskno = 1
elif  wordlen > 3 and wordlen < 6:
   maskno = 2
elif wordlen > 5 and wordlen < 6:
   maskno = 3
elif wordlen > 6 and wordlen < 11:
   maskno = 5
elif wordlen > 11: 
   maskno = 7   
              
randindex = random.sample(range(1, wordlen), maskno)
for i in word:
    maskedword = word.replace(i, "_", maskno)


print(index)
print(word)
print(wordlen)
print(maskno)
print(randindex)
print(maskedword)
