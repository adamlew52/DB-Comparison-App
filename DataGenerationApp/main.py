import DatabaseControl
import GenerationAndFormatting
import DirectoryNavigation

def main():
    DBSetup()
    DBTEST()
    
    dbName = "db1"
    print("---------------------------------------------------------------------------")
    DatabaseControl.ShowAll(dbName)
    print("---------------------------------------------------------------------------")

    deleteDB = input("would you like to delete the contents of the DB? [y/n]: ")

    if deleteDB == "y":
        idList = DatabaseControl.GetRowCount(dbName)
        print("dbName: ",dbName,"idList: ",idList)
        DatabaseControl.ClearDB(dbName, idList)
        DatabaseControl.GetRowCount(dbName)
        #DatabaseControl.ShowAll(dbName)

    print("---------------------------------------------------------------------------")        



def DBSetup():
    print("Setting up DB...")
    dbName = "db1"
    newTableName = "testtable"
    DatabaseControl.CheckDBExist(dbName, newTableName)


#adding data from the generation to the DB
    #IMPORTANT: track the upload times between the following methods
        #1. appending as it is generated
        #2. adding all data to a txt file then uploading the txt file
    
    #method 1
def DBTEST():
    dbName = "db1"
    tableName = "testtable"
    size = 10
    GenerationAndFormatting.PopulateDB(dbName, tableName, size)

#directory navigation and usage
    #DirectoryNavigation.main()

#launch UI and fix handle errors


main()
