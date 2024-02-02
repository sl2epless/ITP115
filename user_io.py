# ITP 115, Fall 2023
# Final Project
# Name: Jingu Lee
# Email: jingulee@usc.edu
# Section: 31867
# Filename: user_io.py
# Description: This program creates various functions that interface with the user. It includes
# creating an options dict, displaying the menu or the information of a language, getting user inputs,
# finding a language based on a phrase, etc.


import helper


# Parameter: a string that will be the name of the text file to read. Has a default value.
# Return: a dictionary where the keys are options (strings) and the values are descriptions (strings)
# This function will create a dictionary of options the user can choose from by reading a file.
def createOptionsDict(textFileStr="menu_options.txt"):
    result = {}
    optionFile = open(textFileStr, 'r')
    for lines in optionFile:
        lines = lines.strip().split(":")
        result[lines[0]] = lines[1]
    optionFile.close()
    return result


# Parameter: a dictionary the options and their descriptions that will be displayed to the user
# Return: None. This function will display the options for the user, using a given dictionary
# This function will display the menu in the options dictionary to the user.
def displayUserMenu(optionsDict):
    keyList = list(optionsDict.keys())
    keyList.sort()
    for keys in keyList:
        print(keys, "->", optionsDict[keys])


# Parameter: a dictionary with the user's options. Return: a string that is
# a valid option entered by the user. This function will get an input from the user to let them choose
# an option from the dictionary
def getUserOption(optionsDict):
    userChoice = input("Option: ").upper().strip()
    while userChoice not in list(optionsDict.keys()):
        userChoice = input("Option: ").upper().strip()
    return userChoice


# Parameter:a list of dictionaries where each dictionary represents a computer language
# Return: None. This function will display the computer languages.
# This function will display the type of all the languages.
def displayType(dataList):
    typeList = helper.getUniqueValues(dataList, 'type')
    print("The", len(typeList), "unique types are")
    for type in typeList:
        print("\t" + type)


# Parameter: a list of dictionaries where each dictionary represents a computer language. Return: None.
# This function will print the total number of programming languages.
def displayNumProgLangs(dataList):
    count = 0
    for dict in dataList:
        if dict['type'] == "programming":
            count += 1
    print("The total number of programming languages is", count)


# Parameter: a dictionary containing information about one computer language. Return: None.
# This function will display the information of a specific language given by langDict
def displayLanguage(langDict):
    print(langDict['title'], " [#", langDict['rank'], "]", sep='')
    if langDict['type'] != "NA":
        print("\t", "Type is ", langDict['type'], sep='')
    if langDict['appeared'] != "NA":
        print("\t", "First appeared in ", langDict['appeared'], sep='')
    if langDict['creators'] != "NA":
        creatorsList = langDict['creators'].split(" and ")
        if len(creatorsList) <= 2:
            print("\t", "Created by ", " and ".join(creatorsList), sep='')
        else:
            print("\t", "Created by ", ", ".join(creatorsList), sep='')
    if langDict['file_extensions'] != "NA":
        print("\t", "File extensions are ", langDict['file_extensions'], sep='')
    if langDict['jobs'] != "NA" and int(langDict['jobs']) > 0:
        print("\t", "Number of jobs is ", langDict['jobs'], sep='')
    if langDict['users'] != "NA" and int(langDict['users']) > 0:
        print("\t", "Number of users is ", langDict['users'], sep='')


# Parameter: a list of dictionaries where each dictionary represents a computer language. Return: None.
# This function will display the oldest function
def displayOldestLanguage(dataList):
    oldestLang = helper.smallestValue(dataList, "appeared")
    displayLanguage(oldestLang)


# Parameter: a list of dictionaries where each dictionary represents a computer language. Return: None
# This function will display the language with the largest number of jobs
def displayMostJobs(dataList):
    largestLang = helper.largestValue(dataList, "jobs")
    displayLanguage(largestLang)


# Parameter: a list of dictionaries where each dictionary represents a computer language. Return: None.
# This function will write a text file the rank of Python and a few sentences about Python
def writeTextFile(dataList):
    rank = "-1"
    for dict in dataList:
        if dict['id'] == 'python':
            rank = dict['rank']
    fout = open("lee_jingu.txt", 'w')
    print("Python is rank #" + rank, file=fout)
    print("Python allows you to store different types of values in a list", file=fout)
    print("Python has a cool name, driven from the name of a large snake", file=fout)
    print("Information was saved to", "lee_jingu.txt")
    fout.close()


# Parameter: a list of dictionaries where each dictionary represents a computer language. Return: None
# This function will allow the user to find a language that includes a user phrase in its information
def findLanguages(dataList):
    count = 0
    phrase = input("Enter a search phrase: ").lower().strip()
    for dict in dataList:
        if phrase in dict['id'].lower() or phrase in dict['title'].lower() or phrase in dict['file_extensions'].lower():
            displayLanguage(dict)
            count += 1
    if count == 0:
        print("No languages contain", "\'" + phrase + "\'")
    else:
        print("Found", count, "languages that contain", "\'" + phrase + "\'")
