# Made by Lucien Hammond
# Using 

import sys, time, random, os
from dice import dice


die = dice()

# Main Loop

while True:
    diePreference = input('What die do you to roll?: ')
    scorePreference = input('Enter ability score want: ')
    
    die.roll(int(diePreference), int(scorePreference))
    
    
