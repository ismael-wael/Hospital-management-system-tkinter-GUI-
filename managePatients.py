from tkinter import *
import tkinter as tk 
from tkinter import ttk
from GUI_Functions import *
import xlsxwriter
import xlrd
from helperFunctions import *

holdPatientData = []

headings = ["patient ID", "Dep. Name", "Doctor", "Name","Age",
            "Gender", "Address", "Room number", "phone number", "diagnose"]

def addPatient(y):
    global holdy
    holdy = y
    global addPatientWindow
    addPatientWindow = Toplevel()
    addPatientWindow.geometry("320x300+1000+100")
    addPatientWindow.title("Add patient")
    y.withdraw()
    addPatientWindow.protocol("WM_DELETE_WINDOW",retriveAdminFromAdd)

    global headings

    #clear old data in holdPatientData
    holdPatientData.clear()
    
    row = 20
    for heading in headings :
        Create_label(addPatientWindow,heading + " : " ,("Times New Roman", 10) , 20, row)
        entry , z = Create_Entry(addPatientWindow , 25 , 110 ,row)
        holdPatientData.append(entry)
        row += 20
        
    Create_button(addPatientWindow, 15 , "Submit" , addPatientFunc
                  , ("Times New Roman", 10) , 20 , 240)
    
def deletePatient(y):
    global holdy
    holdy = y
    global deletePatientWindow
    deletePatientWindow = Toplevel()
    deletePatientWindow.geometry("300x100+1000+100")
    deletePatientWindow.title("Delete patient")
    y.withdraw()
    deletePatientWindow.protocol("WM_DELETE_WINDOW",retriveAdminFromDelete)

    Create_label(deletePatientWindow,"Enter patient ID :" ,("Times New Roman", 10) , 10, 20)

    global patientID
    patientID , z = Create_Entry(deletePatientWindow , 25 , 120 ,20)    

    Create_button(deletePatientWindow, 15 , "Submit" , deletePatientFunc
                  , ("Times New Roman", 10) , 10 , 60)
    
def editPatient(y):
    global holdy
    holdy = y
    global editPatientWindow
    editPatientWindow = Toplevel()
    editPatientWindow.geometry("320x350+1000+100")
    editPatientWindow.title("Edit patient")
    y.withdraw()
    editPatientWindow.protocol("WM_DELETE_WINDOW",retriveAdminFromEdit)

    Create_label(editPatientWindow,"Enter patient ID :" ,("Times New Roman", 10) , 10, 20)

    global patientID
    patientID , z = Create_Entry(editPatientWindow , 25 , 120 ,20)    

    Create_button(editPatientWindow, 15 , "Submit" , editPatientFunc
                  , ("Times New Roman", 10) , 10 , 60)

def displayPatient(y):
    global holdy
    holdy = y
    global displayPatientWindow
    displayPatientWindow = Toplevel()
    displayPatientWindow.geometry("300x300+1000+100")
    displayPatientWindow.title("Display patient")
    y.withdraw()
    displayPatientWindow.protocol("WM_DELETE_WINDOW",retriveAdminFromDisplay)

    Create_label(displayPatientWindow,"Enter patient ID :" ,("Times New Roman", 10) , 10, 20)

    global patientID
    patientID , z = Create_Entry(displayPatientWindow , 25 , 120 ,20)    

    Create_button(displayPatientWindow, 15 , "Submit" , displayPatientFunc
                  , ("Times New Roman", 10) , 10 , 60)

def displayAllPatient(y):
    global holdy
    holdy = y
    global displayAllPatientWindow
    displayAllPatientWindow = Toplevel()
    displayAllPatientWindow.geometry("300x300+1000+100")
    displayAllPatientWindow.title("All patient")
    y.withdraw()
    displayAllPatientWindow.protocol("WM_DELETE_WINDOW",retriveAdminFromDisplayAll)
    
    text = CreateTextScrollbar(displayAllPatientWindow , 300 , 300)
    
    # Give the location of the file
    loc = ("patientsRecords.xlsx")
 
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
    global headings
 
    # For row 1 and column 0
    row = 1
    col = 0
    while sheet.cell_value(row, col) != "EOF" :
        while col < 10 :
            text.insert("end", headings[col] + " : ")
            text.insert("end", sheet.cell_value(row, col))
            text.insert("end", '\n')
            col += 1
        text.insert("end", '******************************\n')
        col = 0
        row += 1   

####################################################################################
def addPatientFunc():
    if checkIfExist(holdPatientData[0].get(),"patientsRecords.xlsx",0):#edit existing entry
        Create_label(bookAppointmentWindow,"Aleardy Exist!",("Times New Roman", 10) , 150, 240)
        Create_label(bookAppointmentWindow,"(ID must be unique)",("Times New Roman",10),150,260)
    else :#new entry
        newEntry("patientsRecords.xlsx",holdPatientData,10)
            
def deletePatientFunc():
    global patientID
    if checkIfExist(patientID.get(),"patientsRecords.xlsx",0) :
        deleteEntry(patientID.get(),"patientsRecords.xlsx",10)
        #clear last writings here ("Not Found!")
        Create_label(deletePatientWindow,"                                " ,
                     ("Times New Roman", 10) , 150, 60)
        #clean writing
        Create_label(deletePatientWindow,"Done!" ,("Times New Roman", 10) , 150, 60)
    else:
        Create_label(deletePatientWindow,"Not Found!" ,("Times New Roman", 10) , 150, 60)

def editPatientFunc():
    global patientID
    if checkIfExist(patientID.get(),"patientsRecords.xlsx",0) :
        index = returnRowNum(patientID.get(),"patientsRecords.xlsx")
        oldData = []

        # Give the location of the file
        loc = ("patientsRecords.xlsx")
 
        # To open Workbook
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        
        col = 0
        while col < 10 :
            oldData.append(sheet.cell_value(index, col))
            col += 1

        #delete old data from fileSystem
        deleteEntry(patientID.get(),"patientsRecords.xlsx",10)

        #clear data in holdPatientData dict
        holdPatientData.clear()

        global headings
            
        row = 90
        i = 0
        for heading in headings :
            Create_label(editPatientWindow,heading + " : " ,("Times New Roman", 10) , 10, row)
            x , z = Create_Entry(editPatientWindow , 25 , 110 ,row)
            holdPatientData.append(x)
            x.set(oldData[i])
            row += 20
            i += 1
        
        Create_button(editPatientWindow, 15 , "Submit" , addPatientFunc
                  , ("Times New Roman", 10) , 10 , 300)
               
    else:
        Create_label(editPatientWindow,"Not Found!" ,("Times New Roman", 10) , 150, 60)

def displayPatientFunc():
    global patientID
    if checkIfExist(patientID.get(),"patientsRecords.xlsx",0) :
        global headings
        printRow(displayPatientWindow ,returnRowNum(patientID.get(),"patientsRecords.xlsx")
                     ,"patientsRecords.xlsx",headings,10)
    else:
        Create_label(displayPatientWindow,"Not Found!" ,("Times New Roman", 10) , 150, 60)

###########################################################################
    
def retriveAdminFromAdd():
    global holdy
    global addPatientWindow
    holdy.deiconify()
    addPatientWindow.destroy()
    
def retriveAdminFromEdit():
    global holdy
    global editPatientWindow
    holdy.deiconify()
    editPatientWindow.destroy()
    
def retriveAdminFromDelete():
    global holdy
    global deletePatientWindow
    holdy.deiconify()
    deletePatientWindow.destroy()
    
def retriveAdminFromDisplay():
    global holdy
    global displayPatientWindow
    holdy.deiconify()
    displayPatientWindow.destroy()
    
def retriveAdminFromDisplayAll():
    global holdy
    global displayAllPatientWindow
    holdy.deiconify()
    displayAllPatientWindow.destroy()



