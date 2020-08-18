import csv

def LoadCSV(filepath, fileDelimeter=','):
    with open(filepath) as csvFile:
        fileRows = []
        reader = csv.reader(csvFile)
        for row in reader:
            fileRows.append(row)

        return fileRows

def ParseCSV(fileRows):
    collumnSize = len(fileRows[0])
    rowsAreEqual = True
    collumns = []
    for row in fileRows:
        if len(row) != collumnSize:
            rowsAreEqual = False
    for col in range (0, collumnSize):
        collumns.append([i[col] for i in fileRows])
    
    return (rowsAreEqual, collumnSize, collumns, fileRows)
    
