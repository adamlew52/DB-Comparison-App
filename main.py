import dbControl
import TrendFinder

#db1Name = input("Please enter the name of the first db you would like to compare: ")
#db2Name = input("Please enter the name of the second db you would like to compare: ")

db1Name = "db1"
db2Name = "db2"

dbData1 = dbControl.db1Import(db1Name)
dbData2 = dbControl.db2Import(db2Name)

dbData1Array = dbControl.parseData(dbData1)
dbData2Array = dbControl.parseData(dbData2)

# ask the user what they would like to compare
# ^include^ display the types of data being stored in the db's

#dataName1 = "data1"
#dataName2 = "data2"
#dbControl.compareData(dataName1,dataName2,db1Name,db2Name,dbData1Array,dbData2Array)


#Trend Finder processing
#TrendFinder.findDifferences(dbData1Array, dbData2Array)
