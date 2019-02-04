# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 17:32:09 2019

@author: edwinaw
"""

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
def maskingIndex(randword):
    wordlen = len(word)
       
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

    
    return randindex 

def masking(randword, maskedIndexNo):
    for i in maskedIndexNo:
        randword = randword.replace(randword[i], "_")
    return randword 



#this function checks whether the input provided matches a missing letter

#Declaring variables from a function
maskedIndexNo = maskingIndex(word)

#Prompts and displays
print(word)
print("Welcome to Hangman")
maskedWord = masking(word, maskedIndexNo)
print(maskedWord)
print("Guess the letters of the missing words, you get " + str(maxGuess) + " guesses")
usrinput = input()

#print(maskedIndexNo)
#
#for i in maskedIndexNo:
#    if word[i] == usrinput:
#        unmaskindex = []
#        unmaskindex.append(i)
#
#print(unmaskindex)
#
#for i in unmaskindex:
#    newword = maskedWord.replace(maskedWord[i], usrinput)
#
#print(newword)

randomLetters =  random.choice(word)
print(randomLetters)
        
#for i in unmaskindex: 
#     maskedWord = maskedWord.replace(maskedWord[5], usrinput)  
#        for i in mylist: 
#            maskedWord = maskedWord.replace(maskedWord[i], usrinput)
         
#        print(maskedWord)
#    else: 
#        maxGuess -= 1
#        print("Incorrect guess, you have " + str(maxGuess) + "  number of guesses left, try again")

#        guessAnswer = True
#    else: 
#        guessAnswer = False
#    if word[i] == usrinput:
#        newWord = maskedWord.replace(maskedWord[i], usrinput)
#    else:
#        newWord = maskedWord
        
#    print(word[i])
#print(maskedWord)

