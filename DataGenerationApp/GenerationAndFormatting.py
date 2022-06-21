import random
import DatabaseControl

def low():
    dataRangeLow = 1
    dataRangeHigh = 25        
    return Generation(dataRangeLow, dataRangeHigh)
def middle():
    dataRangeLow = 25
    dataRangeHigh = 75
    return Generation(dataRangeLow, dataRangeHigh)
def high():
    dataRangeLow = 75
    dataRangeHigh = 100
    return Generation(dataRangeLow, dataRangeHigh)
def default():
    return "invalid input"
    
    # make this class capable of generating multiple different kinds of generation patterns (start with low[1-25], middle[25-75], high[75-100] generation)
    # effectively give the user a menu to choose from the different options
    # use these items in 

def GenerationSetup(dataType, dataSets):
    setCounter = 0
    
    while setCounter <= (int(dataSets)-1):
        setCounter += 1
        if (dataType == "low"):
            print(dataType," was selected")
            low()
        elif (dataType == "middle"):
            print(dataType," was selected")
            middle()
        elif (dataType == "high"):
            print(dataType," was selected")
            high()
        else:
            print(dataType," is not a valid input. Please choose from: [low, medium, high]")

def Generation(dataRangeLow, dataRangeHigh): 
    randVal = random.randrange(dataRangeLow, dataRangeHigh, 2)
    print(randVal)
    return randVal

def PopulateDB(dbName, tableName, size):
    for count in range(1, size):
        dbData1 = low()
        dbData2 = middle()
        DatabaseControl.dbAppendData(dbName, dbData1, dbData2)
        count += 1
        print("count: ", count)
    print("Done with PopulateDB()")