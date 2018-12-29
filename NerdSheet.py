# Made by Lucien Hammond





import sys, time, random, os
from dice import dice



die = dice()

# Main Loop

while True:
    x = input('Enter ability score want: ')
    y = input('What die do you to roll?: ')
    die.roll(int(y), int(x))
    
    
