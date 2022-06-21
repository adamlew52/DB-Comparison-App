import filecmp
from logging import exception
import ntpath
import os
from pathlib import Path

#ATTENTION: os libraries may be faulty on windows machines. If you are using Mac or Linux please check the ReadMe, section 2 for recommendations


#TODO
# - finish selectCSV...we're so close. The for loops needs tweaked, the problem with python for loops is that they iterate through strings in an unfamiliar way. 
#   shouldnt be toooooo hard to fix tho, its just 3:08am and i have class and work in the morning
# - return the selected numbers from selectCSV back to main. Call GenerationAndFormatting.py to populate the selected files
#       - IMPORTANT: be sure to utilize the function that checks to see if the DB has tables and is formatted to recieve the data
# - add a function that checks to make sure that the DB was completely populated
# 


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

    print(csvFiles)
    return csvFiles

def SelectCSV(csvFileArray):
    selectedFiles = input("\nPlease enter the number(s) corresponding to the .csv file you would like populate\nFor multiple files, please be sure to use the format of (#,#,..,#): ")
    csvFileArrayLength = len(csvFileArray)
    selectedFiles = selectedFiles.split(",")

    try:
        print("try start")
        print("")
        for selectedElement in selectedFiles:
            print("type(selectedElement): ",type(selectedElement),"in iteration",selectedElement)
            print("type(selectedFiles): ",type(selectedFiles),"in iteration",selectedElement)
            
            res = [ele for ele in selectedFiles if(ele in selectedFiles)]

            if res:
                print("this is matching")
                selectedElement = int(selectedElement)
                print("selectedElement: ",selectedElement)
                print("csvFileArray[selectedElement]: ",csvFileArray[selectedElement])
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
