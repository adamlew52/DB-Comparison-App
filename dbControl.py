import sqlite3

def db1Import(db1Name):
    print("importing data from", db1Name)
    dbDataImport1 = (db1Name + ".db")
    conn1 = sqlite3.connect(dbDataImport1)
    c1 = conn1.cursor() 

    c1.execute("SELECT rowid, * FROM 'Test Table'")
    items =  c1.fetchall()
    items1Array = []

    for item in items:
        items1Array.append(item)

    conn1.commit()
    conn1.close()
    return items1Array

def db2Import(db2Name):
    print("importing data from", db2Name)
    dbDataImport2 = (db2Name + ".db")
    conn2 = sqlite3.connect(dbDataImport2)
    c2 = conn2.cursor() 

    c2.execute("SELECT rowid, * FROM 'Test Table'")
    items =  c2.fetchall()
    items2Array = []

    for item in items:
        items2Array.append(item)

    conn2.commit()
    conn2.close()
    return items2Array

def parseData(dataArray):
    testArray = [] #info is parsed into THIS array from the imported data from the DB
    yRef = 0
    while yRef < (len(dataArray)):
        position = dataArray[yRef][0]
        valueOne = dataArray[yRef][1]
        valueTwo = dataArray[yRef][2]

        testArray.append(position)
        testArray.append(valueOne)
        testArray.append(valueTwo)

        print("FLAG - testArray:",testArray)
        yRef += 1  

    return testArray
    
def compareData(dataName1,dataName2,db1Name,db2Name,dbData1Array,dbData2Array):
    db1Name = (db1Name + ".db")
    db2Name = (db2Name + ".db")

    conn1 = sqlite3.connect(db1Name)
    conn2 = sqlite3.connect(db2Name)
    c1 = conn1.cursor() 
    c2 = conn2.cursor() 

    #print("Attempt to find table info:",c1.execute("""PRAGMA table_info('Test Table');"""))

    positionInDB1 = 2
    positionInDB2 = 2

    print("\nNumber 1 and Number 1 are being compared")
    valueOne = dbData1Array[1]
    valueTwo = dbData2Array[1]
    print(valueOne, "vs", valueTwo)
    comparison = compareSize(valueOne, valueTwo)
    print(comparison)

    print("\nNumber 2 and Number 2 are being compared")
    valueOne1 = dbData1Array[positionInDB1]
    valueTwo2 = dbData2Array[positionInDB2]
    print(valueOne1, "vs", valueTwo2)
    print(compareSize(valueOne1, valueTwo2))
    
    print("\nthe values have been compared")

    conn1.commit()
    conn2.commit()
    conn1.close()
    conn2.close()


def compareSize(valueOne, valueTwo):
    if valueOne > valueTwo:
        outcome = "value one is greater than value two"
    elif valueOne < valueTwo:
        outcome = "value two is greater than value one"
    elif valueOne == valueTwo:
        outcome = "the two values are equal"

    return outcome 
