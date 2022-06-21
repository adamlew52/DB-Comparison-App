import filecmp
from logging import exception
import ntpath
import os
from pathlib import Path

#ATTENTION: os libraries may be faulty on windows machines. If you are using Mac or Linux please check the ReadMe, section 2 for recommendations


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
    while (dirInput != ["X","x"]):
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
    return csvFiles

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
        findCSV(directoryAddress)

    else: 
        print("nothing input")
        Menu()
        

Menu()
