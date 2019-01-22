# Made by Lucien Hammond
# Using 

import sys, time, random, os
from dice import dice
import database

die = dice()

# Main Loop

while True:
    '''
    diePreference = input('What die do you to roll?: ')
    scorePreference = input('Enter ability score want: ')
    
    die.roll(int(diePreference), int(scorePreference))
    '''


    '''
    database.set('test', 'This is a test\n')
    database.set('test', 'to see if we can do multiple lines')
    break
    '''
    '''
    test = database.getlist('test', ' ')
    # Stuff in your inventory
    inventory = database.getlist('inventory', ' ')
    # Stuff on the top bar
    topBar = database.getlist('topBar', ' ')
    # Main ability scores
    abilityScores = database.getlist('abilityScores', ' ')
    # Ability modifiers for actions
    abilityModifiers = database.getlist('abilityModifiers', ' ')
    # Health, AC, etc
    combat = database.getlist('combat', ' ')
    # Spell modifiers
    spellModifiers = database.getlist('spellModifiers', ' ')
    # Spell List
    spellList = database.getlist('spellList', ' ')
    break
    '''
    arr = ['Hello', 'Friend', 'How', 'Are', 'You', 'Gottem']
    database.setlist('listTest', arr)
    break
