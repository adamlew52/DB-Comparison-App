import filecmp
from logging import exception
import ntpath
import os
from pathlib import Path
import GenerationAndFormatting
import DatabaseControl
import CustomTableCreation

#ATTENTION: os libraries may be faulty on windows machines. If you are using Mac or Linux please check the ReadMe, section 2 for recommendations

#Purpose:
#to allow the user to access the directory of the project(s) they will be working on. 
# Secondary Feature: connects the directory to the program that populates the databases


#TODO
# - finish selectCSV

#BUG
# line37 THERE IS NEVER A CASE FOR DIRINPUT TO BE CHANGED IN THIS CASE. FIX THIS ERROR

#error handling
class Error(Exception):
    """Not Really Sure What Happened. Read the Log"""
    pass
    
class InvalidDirectory(Error):
    """Invalid input please try again"""
    pass


#functions used in operation
def GetProjectDirectory():
    dirInput = input("Please enter pathing to the root directory of your project. Type 'CWD' if you are using the Current Working Directory: ")
    while (dirInput != ["X","x"]): #THERE IS NEVER A CASE FOR DIRINPUT TO BE CHANGED IN THIS CASE. FIX THIS ERROR #BUG
        try:
            if dirInput in ["cwd","Cwd","CWd","CWD","cWd","cWD","cwD"]:
                directoryAddress = os.getcwd()
                print("Working Directory Set to CWD aka:", directoryAddress)
                break
            elif os.path.isdir(dirInput):
                directoryAddress = dirInput
                print("Working Directory Set:", directoryAddress)
                break
            else:
                raise InvalidDirectory
        except InvalidDirectory:
            Menu()
    return directoryAddress

def findCSV(directoryAddress):
    csvFiles = []
    files = Path().cwd().glob("**/*.csv")

    for f in files:
        baseName =  ntpath.basename(f)
        splitFileName = os.path.splitext(baseName)
        formattedFileName = (splitFileName[0])
        csvFiles.append(formattedFileName)

    print(csvFiles)
    return csvFiles

def DBPopulation(dbName, tableName, size):
    GenerationAndFormatting.PopulateDB(dbName, tableName, size)

def SelectCSV(csvFileArray):
    selectedFiles = input("\nPlease enter the number(s) corresponding to the .csv file you would like populate\nFor multiple files, please be sure to use the format of (#,#,..,#): ")
    selectedFiles = selectedFiles.split(",")

    try:
        print("try start")
        print("")

        tableName = "TT "
        for selectedElement in selectedFiles:
            print("iteration: ",selectedElement)
            
            res = [ele for ele in selectedFiles if(ele in selectedFiles)] #res = bool; tests if the input number has a corresponding element

            if res:
                selectedElement = int(selectedElement)
                print("this is matching the element ",csvFileArray[selectedElement])
                
                size = 1000
                dbName = csvFileArray[selectedElement]
                tableName = (tableName+selectedElement) # if number 1 and 3 are chosen then "TT TESTCSV" and "TT TESTME3" will be created respectively

                CustomTableCreation.CreateTable(dbName, tableName)
                GenerationAndFormatting.PopulateDB(csvFileArray[selectedElement], tableName, size)
            else:
                print("not selected: ",csvFileArray[selectedElement])
            print("")
        
        print("end try")
    except:
        print("except placeholder")
    
    print("code continued...")

def Menu():
    directoryAddress = GetProjectDirectory()
    menuSelect = 0
    
    #this part of the code will allow the user to see all of the contents in a directory
    print("")
    print("The Directory ",directoryAddress," has been chosen")
    print("")
    menuSelect = input("Menu\n[1] Automatically find all .CSV files in the chosen directory\n[2] Create a new .CSV project\n[3]\n[4]\n\nSelection: ")
    print("")
    if(menuSelect == "1"):
        print("option 1 selected")
        SelectCSV(findCSV(directoryAddress))

    else: 
        print("nothing input")
        Menu()
        
Menu()