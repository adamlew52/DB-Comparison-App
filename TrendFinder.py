import sqlite3
import dbControl

def findDifferences(dbData1Array, dbData2Array):
    print("findDifferences dbData1Array", dbData1Array)
    print("findDifferences dbData1Array[5]:", dbData1Array[5])
    
    print("findDifferences dbData2Array", dbData2Array)
    print("findDifferences dbData2Array[0]:", dbData2Array[0])

    compareCounter = 1
    print("comparing the values in the first database")
    while compareCounter < len(dbData1Array):
        diffCalc = (dbData1Array[compareCounter] - dbData1Array[compareCounter-1])
        print("The difference between value in position",compareCounter,"and its prior number is ", diffCalc)
        compareCounter+=1
    
    compareCounter = 1
    print("\n\ncomparing the values in the second database")
    while compareCounter < len(dbData2Array):
        diffCalc = (dbData2Array[compareCounter] - dbData2Array[compareCounter-1])
        print("The difference between value in position",compareCounter,"and its prior number is ", diffCalc)
        compareCounter+=1

