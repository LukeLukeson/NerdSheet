# Variable Database
# Using some code made by Matthew Galant

import os



'''
with open(key + '.data') as f:
    content = f.readlines()

content = [x.strip() for x in content]
'''
'''
# Creates a file and writes data for the file
def set(key, data):

    # Creates location for the saved files if one doesn't exist
    if not os.path.exists(".pydb/"):
        os.makedirs(".pydb/")

    # Opens file with append
    dataStore = open(".pydb/" + key + ".data", "a+")

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
'''
# Lists all files in .pyDB
def listfiles():
    entries = []
    for file in os.listdir(".pydb/"):
        if file.endswith(".data"):
            entries.append(file[0:-5])
    return entries

# Puts an array into a file
def setlist(key, list):
    if not os.path.exists('.pydb/'):
        os.makedirs('.pydb/')
    dataStore = open(".pydb/" + key + ".data", "a+")
    for x in list:
        dataStore.write(str(x) + '\n')
    dataStore.close()

# Reads what is currently in a file and puts it into an array
def getlist(key, listN):
    with open(".pydb/" + key + '.data') as f:
        listN = f.readlines()
    listN = [x.strip() for x in listN]
    return listN
    
# Replaces file with updated array
def savelist():
    pass

def removelist():
    pass
