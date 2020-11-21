from tkinter import *
import tkinter as tk 
from tkinter import ttk
from GUI_Functions import *
import xlsxwriter
import xlrd

def newEntry(fileName , hold,numberOfElements):
    #add patient a new patient to the dictionary
    newData = dict()
    oldData = dict()
    temp = []
    for i in hold :
        temp.append(i.get())
    newData[hold[0].get()] = temp[1:]

    #restore old data
    oldData = retainOldData(0,"EOF",fileName,numberOfElements)
    
    #create new file
    writeNewData(oldData, newData,fileName,numberOfElements)

def deleteEntry(ID,fileName,numberOfElements):
    beforeID = dict()
    afterID  = dict()
    beforeID = retainOldData(0,ID,fileName,numberOfElements)
    afterID = retainOldData(returnRowNum(ID,fileName) + 1,"EOF"
                            ,fileName,numberOfElements)

    #create new file
    writeNewData(beforeID, afterID,fileName,numberOfElements)

def checkIfExist(ID , fileName,col):
    # Give the location of the file
    loc = (fileName)
 
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    # For row 1
    row = 1
    while sheet.cell_value(row, 0) != "EOF" :
        key = sheet.cell_value(row, col)
        if key == ID:
            return True
        row += 1

    return False

def returnRowNum(ID,fileName):
    # Give the location of the file
    loc = (fileName)
 
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    # For row 1
    row = 1
    while sheet.cell_value(row, 0) != "EOF" :
        key = sheet.cell_value(row, 0)
        if key == ID:
            return row
        row += 1

def retainOldData(start,end,fileName,numberOfCols):
    oldData = dict()
    
    # Give the location of the file
    loc = (fileName)
 
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
 
    # For row 0 and column 0
    row = start
    col = 0
    while sheet.cell_value(row, col) != end :
        key = sheet.cell_value(row, col)
        temp = []
        col += 1
        while col < numberOfCols:
            temp.append(sheet.cell_value(row, col))
            col += 1
        oldData[key] = temp
        col = 0
        row += 1

    return oldData

def writeNewData (oldData, newData,fileName,numberOfCols):
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(fileName)
    worksheet = workbook.add_worksheet()     

    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0

    #write the old data
    for key in oldData.keys() :
        worksheet.write(row, col,key)
        col += 1
        for value in oldData[key]:
           worksheet.write(row,col,value)
           col += 1
        row += 1
        col = 0

    #write the new data
    for key in newData.keys() :
        worksheet.write(row, col,key)
        col += 1
        for value in newData[key]:
           worksheet.write(row,col,value)
           col += 1
        row += 1
        col = 0

    #end of data  
    while (col < numberOfCols):
        worksheet.write(row,col,"EOF")
        col += 1
    
    workbook.close()

def printRow(window ,rowIndex,fileName,heads , numOfCols):
    # Give the location of the file
    loc = (fileName)
 
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    holdData = []
    i = 0
    while i < numOfCols:
        holdData.append(sheet.cell_value(rowIndex, i))
        i += 1
    i = 0
    row = 90
    for j in heads :
        Create_label(window,j + " : " ,("Times New Roman", 10) , 20, row)
        Create_label(window,holdData[i],("Times New Roman", 10) , 110, row)
        row += 20
        i += 1
