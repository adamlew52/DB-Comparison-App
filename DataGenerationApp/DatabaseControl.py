import sqlite3


def CheckDBExist(dbName, newTableName):
    dbDataImport1 = (dbName + ".db")
    try:
        conn = sqlite3.connect(dbfDataImport1)
        print("Successfully connected to the DB")
        c = conn.cursor()
    
    except sqlite3.Error as error:
        print("Failed to connect to the table. Error: ", error , "Creating a new table: ")
        createTable = '''CREATE TABLE testtable(
            FIRSTDATA INT
            SECONDDATA INT    
        )'''
        c.execute(createTable)
        conn.commit()
        conn.close()

def DBExist(db1Name):
    #temp code
    print("checking if ",db1Name, "exists in the directory...")

def DBCreate(dbName):
    #temp code
    print("creating database: ",dbName, "in the user's directory...")

def db1Import(db1Name):
    print("importing data from", db1Name)
    dbDataImport1 = (db1Name + ".db")
    conn1 = sqlite3.connect(dbDataImport1)
    c1 = conn1.cursor() 

    c1.execute("SELECT rowid, * FROM 'Test Table'")
    items =  c1.fetchall()
    items1Array = [[],[]]

    for item in items:
        items1Array.append(item)

    conn1.commit()
    conn1.close()
    return items1Array

def dbAppendData(dbName, dbData1, dbData2):
    dbDataImport1 = (dbName + ".db")
    conn = sqlite3.connect(dbDataImport1)
    c = conn.cursor() 
    c.execute("INSERT INTO testtable VALUES (?,?)", (dbData1,dbData2))
    conn.commit()
    conn.close()

def ShowAll(dbName):
    dbDataImport1 = (dbName + ".db")
    conn = sqlite3.connect(dbDataImport1)
    c = conn.cursor()
    
    c.execute("SELECT rowid, * FROM testtable")
    items = c.fetchall()

    for item in items:
        print(item)    
    
    conn.commit()
    conn.close()

def ClearDB(dbName, idCount):
    dbDataImport1 = (dbName + ".db")

    try: 
        conn = sqlite3.connect(dbDataImport1)
        c = conn.cursor()

        c.execute("DROP TABLE testtable")
        print("Dropped testable")
        # Creating table
        table = """ CREATE testtable (
                    Column1 INT NOT NULL,
                    Column2 INT NOT NULL
                ); """
 
        c.execute(table)
        print("created new testtable")

        conn.commit()
        print("         Record deleted successfully...")
    
    except sqlite3.Error as error:
        print("Failed to delete the record from the table. Error Code: ", error)

    conn.commit()
    conn.close()

def GetRowCount(dbName):
    dbDataImport1 = (dbName + ".db")
    conn = sqlite3.connect(dbDataImport1)
    c = conn.cursor()

    c.execute("SELECT * FROM testtable")
    
    rowCountResult = len(c.fetchall())

    print(rowCountResult)
    
    conn.commit()
    conn.close()
    print("rowCountResult: ",rowCountResult)
    return rowCountResult



#testing
dbName = "db1"
tableName = "testtable"

#ClearDB("db1", 100)
CheckDBExist(dbName, tableName)