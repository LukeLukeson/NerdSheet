# Made by Lucien Hammond

import sys, time, random, os
from dice import dice



die = dice()

# Main Loop

while True:
    x = input('Enter ability score want: ')
    y = input('What die do you  to roll?: ')
    
    if int(x) > -20 and int(x) < 20:
        die.roll(int(y), int(x))
    else:
        print('What are you doing that requires you to have that as an ability score?!?!?!?')
        time.sleep(1)

    
