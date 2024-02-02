# ITP 115, Fall 2023
# Final Project
# Name: Jingu Lee
# Email: jingulee@usc.edu
# Section: 31867
# Filename: main_lee_jingu.py
# Description: This program allows the user to learn about computer languages. It reads a CSV
# (comma-separated values) file with information about computer languages to create a list of
# dictionaries. Each dictionary holds the information for one computer language where the
# keys are strings and the values are strings


import helper
import user_io
import extra_credit


# No parameter or return value. This is a main function that will call various functions and let the user
# make an input, or etc.
def main():
    print("Learn about computer languages")
    dataList = helper.createDataList()
    optionsDict = user_io.createOptionsDict()
    user_io.displayUserMenu(optionsDict)
    userOption = user_io.getUserOption(optionsDict)
    while userOption != 'Q':
        if userOption  == 'A':
            user_io.displayType(dataList)
        elif userOption == 'B':
            user_io.displayNumProgLangs(dataList)
        elif userOption == 'C':
            user_io.displayOldestLanguage(dataList)
        elif userOption == 'D':
            user_io.displayMostJobs(dataList)
        elif userOption == 'E':
            user_io.writeTextFile(dataList)
        elif userOption == 'F':
            user_io.findLanguages(dataList)
        elif userOption == 'G':
            extra_credit.displayIndentLanguages(dataList)
        else:
            extra_credit.displayTopRanked(dataList)
        print()
        user_io.displayUserMenu(optionsDict)
        userOption = user_io.getUserOption(optionsDict)


main()