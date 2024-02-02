# ITP 115, Fall 2023
# Final Project
# Name: Jingu Lee
# Email: jingulee@usc.edu
# Section: 31867
# Filename: helper.py
# Description: This program creates a few functions. The functions will read a file and create a data list or
# determine the largest, or the smallest value of a certain category among all the languages.

# Parameter: file name. Default given. Result: a list of dictionaries. Each dictionary includes a category
# and its corresponding information. Each dictionary represents a language.
# This function will create a data list by reading a file. It makes dictionaries each representing a language
# and store it in a list
def createDataList(csvFileStr="computer_languages.csv"):
    result = []
    langFile = open(csvFileStr, 'r')
    keys = langFile.readline().strip().split(',')
    for line in langFile:
        langDict = {}
        line = line.strip().split(",")
        for i in range(len(keys)):
            langDict[keys[i]] = line[i]
        result.append(langDict)
    langFile.close()
    return result

# Parameter: a list of dictionaries and a key string to indicate a key in one of the dictionaries.
# Return: a list of unique values in one category among all the languages.
# This function will find unique values in a category and store them in a list.
def getUniqueValues(dataList, keyStr):
    result = []
    for dict in dataList:
        if dict[keyStr] not in result:
            result.append(dict[keyStr])
    result.sort()
    return result

# Parameter: a list of dictionaries and a key string to indicate a key in one of the dictionaries.
# a dictionary containing one computer language, which has the largest value for the category indicated by
# the key string
# This function will find the largest value in a category among all the languages
def largestValue(dataList, keyStr):
    largest = 0
    result = {'initial':'value'}

    for dict in dataList:
        if dict[keyStr].isdigit():
            if int(dict[keyStr]) > largest:
                largest = int(dict[keyStr])
                result = dict
    return result


# Parameter: a list of dictionaries and a key string to indicate a key in one of the dictionaries.
# a dictionary containing one computer language, which has the smallest value for the category indicated by
# the key string
# This function will find the smallest value in a category among all the languages.
def smallestValue(dataList, keyStr):
    smallest = None
    result = {'initial':'value'}

    for dict in dataList:
        if dict[keyStr].isdigit():
            if smallest is None or int(dict[keyStr]) < smallest:
                smallest = int(dict[keyStr])
                result = dict
    return result