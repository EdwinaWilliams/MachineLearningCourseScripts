# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 22:55:40 2019

@author: edwinaw
"""


#importing of modules
import random 

#variable declaration
runningGuess = 0
maxGuess = 3
min = 1
max = 47
index = random.randint(min, max)


# Importing random word based on random guess  

with open ("HangManWords.txt") as words: 
    word = words.read().split('\n') [index]


#functions 

#this function receives a word and masks some of the letters     
def masking(randword):
    wordlen = len(randword)
       
    if wordlen >= 1 and wordlen <= 3:
       maskno = 1
    elif  wordlen >= 4 and wordlen <= 6:
       maskno = 2
    elif wordlen >= 7 and wordlen <= 8:
       maskno = 3
    elif wordlen >= 9 and wordlen <= 11:
       maskno = 5
    elif wordlen >= 12 : 
       maskno = 7   
                  
    randindex = random.sample(range(0, wordlen), maskno)
    
    for i in randindex:
        randword = randword.replace(randword[i], "_")
    return randword



#this function checks whether the input provided matches a missing letter

#Prompts and displays
print("Welcome to Hangman")
print(masking(word))
print("Guess the letters of the missing words, you get " + str(maxGuess) + " guesses")
#usrinput = input()


for i in maskedIndexNo:
    if word[i] == usrinput:
        guessAnswer = True
    else: 
        guessAnswer = False
  

print(guessAnswer)
