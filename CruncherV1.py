'''
This is a program made to sort through all the data from the GPS app for the McMaster Baja Racing team
Author: Shaqeeb Momen
Date: Dec. 2017
'''

logFileName = input("File Name: ")
logFile = open(logFileName, "r")

logData = logFile.readlines()
