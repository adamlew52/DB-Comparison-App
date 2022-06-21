import os 

def main():
    if(UserOptions() == 1):
        NavigateDirectory()
    elif(UserOptions() == 2):
        NavigateDirectory()
    elif(UserOptions() == 3):
        NavigateDirectory()
    elif(UserOptions() == 4):
        NavigateDirectory()
    elif(UserOptions() == 1):
        NavigateDirectory()
    else: 
        print("not a real option pussy-fart")

#user options
def UserOptions():
    print("------------------------------------")
    print("               Options")
    print(" 1. Enter a directory address")
    print(" 2. Find a DB in current directory")
    print(" 3. Create a new directory")
    print(" 4. Add a DB")
    print(" 5. Blank for now!")
    print("------------------------------------")

    userOption = input("User option: ")
    return userOption

#navigating directories
def NavigateDirectory():
    directoryName = input("Option 1: Please enter the ENTIRE ADDRESS of the directory you wish to use: ")

#finding existing db in current directory
def SearchDB(dbName):
    print("Option 2: Finding DB ",dbName)

#make a new directory
def CreateDirectory(directoryName):
    print("Option 3: Making Directory: ",directoryName)

#adding a db
def MakeDB(dbName):
    print("Option 4: Making DB: ",dbName)