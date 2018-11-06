# Made by Lucien Hammond
# Using MatthewGallant's PyDB for saving variables

import tkinter, sys, time, random, os

# Rolls a twenty sided die

def rollTwenty(abilityScore):
    twenty = random.randint(1,20)
    if twenty == 20:
        print('Natural 20')
    elif twenty == 1:
        print('Critical Fail')
    else:
        twentyFinal = twenty + int(abilityScore)
        print(str(twenty) + ' + ' + str(abilityScore) + ' = ' + str(twentyFinal)) 

# Rolls a twelve sided die

def rollTwelve(abilityScore):
    twelve = random.randint(1,12)
    twelveFinal = twelve + int(abilityScore)
    print(str(twelve) + ' + ' + str(abilityScore) + ' = ' + str(twelveFinal))

def rollTen():
    pass

def rollEight():
    pass

def rollSix():
    pass

def rollFour():
    pass

def rollHundred():
    pass
    
# Main Loop

while True:
    abilityScore = input('Enter ability score: ')



    if int(abilityScore) > -11 and int(abilityScore) < 11:
        rollTwenty(abilityScore)
    else:
        print('Thats not a valid ability score')
    
