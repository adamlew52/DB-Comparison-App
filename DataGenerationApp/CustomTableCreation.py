import sqlite3
#import DatabaseControl
#import GenerationAndFormatting
#import DirectoryNav

# TODO
# finish "generic table" formatting. probably should have done this first to test the functionality but whatever

#may want to turn this into a class, so different iterations of the class can be called 

def CreateTable(dbName, tableName):
    dbDataImport1 = (dbName + ".db")
    conn = sqlite3.connect(dbDataImport1)
    c = conn.cursor()

    print("[g] for generic table\n[i] for integer table\n[s] for string table (must have .txt file to upload. minimum of 100 words))\n[x] to quit")
    userInput = input("Input: ")
    userInput = userInput.lower()
    
    #be sure to add the table name in here. if we need to move "initialString" out then make it a paramter of CreateTableInt then do it
    
    c.execute(CreateCustomTable(userInput)) #check in DirectoryNav.py for the part finding only .csv files. we may want to convert it to .db files

    conn.commit()
    conn.close()


def CreateCustomTable(userInput):
    initialString = """CREATE TABLE IF NOT EXISTS projects ( 
        id integer PRIMARY KEY,\n"""

    if userInput == "g":
        columnName = input("Enter Column Name: ")
        genericString = (columnName+"")
        creationString = (initialString+ genericString)
        print("FLAG - PLEASE CHECK FORMATTING ON FOLLOWING STRING:\n\t\t"+creationString)

    elif userInput == "i":
        columnName = input("Enter Column Name: ")
        integerString = (columnName+" integer  NOT NULL,\n")
        creationString = (initialString+ integerString)
        print("FLAG - PLEASE CHECK FORMATTING ON FOLLOWING STRING:\n\t\t"+creationString)

    elif userInput == "s":
        columnName = input("Enter Column Name: ")
        stringString = (columnName+"text NOT NULL,\n")
        creationString = (initialString+ stringString)
        print("FLAG - PLEASE CHECK FORMATTING ON FOLLOWING STRING:\n\t\t"+creationString)

    else:
        CreateCustomTable(userInput)

    creationString = (creationString+"\n)")
    print("\t\tcreationString: \n")
    
    return creationString

