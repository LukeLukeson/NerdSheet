# Variable Database
# Using some code made by Matthew Galant

import os

# Creates a file and writes data for the file

def set(key, data):

    # Creates location for the saved files if one doesn't exist
    if not os.path.exists(".pydb/"):
        os.makedirs(".pydb/")

    # Opens file
    dataStore = open(".pydb/" + key + ".data", "w+")

    # Writes Data and closes file
    dataStore.write(str(data))
    dataStore.close()

# Gets data from a file

def get(key):

    # Opens file
    dataStore = open(".pydb/" + key + ".data", "r")

    # Reads file
    data = dataStore.read()

    # Closes file and returns data
    dataStore.close()
    return data

# Deletes data file

def unset(key):
    os.remove(".pydb/" + key + ".data")

# Lists all files in .pyDB

def list():
    entries = []
    for file in os.listdir(".pydb/"):
        if file.endswith(".data"):
            entries.append(file[0:-5])
    return entries