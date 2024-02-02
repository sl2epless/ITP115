# ITP 115, Fall 2023
# Final Project
# Name: Jingu Lee
# Email: jingulee@usc.edu
# Section: 31867
# Filename: user_io.py
# Description: This program creates two function that each display the languages that require indentation
# and the top 10 ranked languages form the 0th to the 9th.


import user_io


# Parameter: a list of dictionaries. Return: none. Displays the languages that requre indentation
def displayIndentLanguages(dataList):
    print("The languages that require indentation are")
    for dict in dataList:
        if dict['indentation'] == 'TRUE':
            print("\t"+dict['title'])


# Parameter: a list of dictionaries. Return: None. Displays the top 10 ranked languages.
def displayTopRanked(dataList):
    print("The top ranked 10 languages are")
    ranksDict = {}
    for dict in dataList:
        rankInt = int(dict['rank'])
        if int(rankInt) <= 9:
            ranksDict[rankInt] = dict

    for i in range(10):
        user_io.displayLanguage(ranksDict[i])
