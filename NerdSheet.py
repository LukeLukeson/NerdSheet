# Made by Lucien Hammond
# Using MatthewGallant's PyDB for saving variables
import tkinter, sys, time, random, os

def rollTwenty(abilityScore):
    twenty = random.randint(1,20)
    if twenty == 20:
        print('Natural 20')
    elif twenty == 1:
        print('Critical Fail')
    else:
        twentyFinal = twenty + int(abilityScore)
        print(str(twenty) + ' + ' + str(abilityScore) + ' = ' + str(twentyFinal)) 


    
while True:
    abilityScore = input('Enter ability score: ')
    rollTwenty(abilityScore)