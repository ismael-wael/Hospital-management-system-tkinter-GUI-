from tkinter import *
import tkinter as tk 
from tkinter import ttk
from GUI_Functions import *
from helperFunctions import *
import xlsxwriter
import xlrd

holdDoctorData = []

headings = ["doctor ID", "Dep. Name", "Name","Address","phone number"]

def addDoctor(y):
    global holdy
    holdy = y
    global addDoctorWindow
    addDoctorWindow = Toplevel(y)
    addDoctorWindow.geometry("320x300+1000+100")
    addDoctorWindow.title("Add Doctor")
    y.withdraw()
    addDoctorWindow.protocol("WM_DELETE_WINDOW",retriveAdminFromAdd)

    global headings 

    #clear old Data in holdDoctorData dict
    holdDoctorData.clear()
    
    row = 20
    for heading in headings :
        Create_label(addDoctorWindow,heading + " : " ,("Times New Roman", 10) , 20, row)
        entry , z = Create_Entry(addDoctorWindow , 25 , 110 ,row)
        holdDoctorData.append(entry)
        row += 20
        
    Create_button(addDoctorWindow, 15 , "Submit" , addDoctorFunc
                  , ("Times New Roman", 10) , 20 , 240)

def deleteDoctor(y):
    global holdy
    holdy = y
    global deleteDoctorWindow
    deleteDoctorWindow = Toplevel(y)
    deleteDoctorWindow.geometry("300x100+1000+100")
    deleteDoctorWindow.title("Delete doctor")
    y.withdraw()
    deleteDoctorWindow.protocol("WM_DELETE_WINDOW",retriveAdminFromDelete)

    Create_label(deleteDoctorWindow,"Enter doctor ID :" ,("Times New Roman", 10) , 10, 20)

    global doctorID
    doctorID , z= Create_Entry(deleteDoctorWindow , 25 , 120 ,20)    

    Create_button(deleteDoctorWindow, 15 , "Submit" , deleteDoctorFunc
                  , ("Times New Roman", 10) , 10 , 60)

def editDoctor(y):
    global holdy
    holdy = y
    global editDoctorWindow
    editDoctorWindow = Toplevel(y)
    editDoctorWindow.geometry("320x350+1000+100")
    editDoctorWindow.title("Edit doctor")
    y.withdraw()
    editDoctorWindow.protocol("WM_DELETE_WINDOW",retriveAdminFromEdit)

    Create_label(editDoctorWindow,"Enter doctor ID :" ,("Times New Roman", 10) , 10, 20)

    global doctorID
    doctorID , z = Create_Entry(editDoctorWindow , 25 , 120 ,20)    

    Create_button(editDoctorWindow, 15 , "Submit" , editDoctorFunc
                  , ("Times New Roman", 10) , 10 , 60)

def displayDoctor(y):
    global holdy
    holdy = y
    global displayDoctorWindow
    displayDoctorWindow = Toplevel(y)
    displayDoctorWindow.geometry("300x300+1000+100")
    displayDoctorWindow.title("Display doctor")
    y.withdraw()
    displayDoctorWindow.protocol("WM_DELETE_WINDOW",retriveAdminFromDisplay)

    Create_label(displayDoctorWindow,"Enter doctor ID :" ,("Times New Roman", 10) , 10, 20)

    global doctorID
    doctorID , z = Create_Entry(displayDoctorWindow , 25 , 120 ,20)    

    Create_button(displayDoctorWindow, 15 , "Submit" , displayDoctorFunc
                  , ("Times New Roman", 10) , 10 , 60)

def displayAllDoctor(y):
    global holdy
    holdy = y
    global displayAllDoctorWindow
    displayAllDoctorWindow = Toplevel(y)
    displayAllDoctorWindow.geometry("300x300+1000+100")
    displayAllDoctorWindow.title("All doctor")
    y.withdraw()
    displayAllDoctorWindow.protocol("WM_DELETE_WINDOW",retriveAdminFromDisplayAll)
    
    text = CreateTextScrollbar(displayAllDoctorWindow , 300 , 300)
    
    # Give the location of the file
    loc = ("doctorsRecords.xlsx")
 
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    global headings
 
    # For row 1 and column 0
    row = 1
    col = 0
    while sheet.cell_value(row, col) != "EOF" :
        while col < 5 :
            text.insert("end", headings[col] + " : ")
            text.insert("end", sheet.cell_value(row, col))
            text.insert("end", '\n')
            col += 1
        text.insert("end", '******************************\n')
        col = 0
        row += 1
################################################################################
def addDoctorFunc():
    if checkIfExist(holdDoctorData[0].get(),"doctorsRecords.xlsx",0):#edit existing entry
        Create_label(bookAppointmentWindow,"Aleardy Exist!",("Times New Roman", 10) , 150, 240)
        Create_label(bookAppointmentWindow,"(ID must be unique)",("Times New Roman",10),150,260)
    else :#new entry
        newEntry("doctorsRecords.xlsx",holdDoctorData,5)

def deleteDoctorFunc():
    global doctorID
    if checkIfExist(doctorID.get(),"doctorsRecords.xlsx",0) :
        deleteEntry(doctorID.get(),"doctorsRecords.xlsx",5)
        #clean last writings ("Not Found!")
        Create_label(deleteDoctorWindow,"                                " ,
                     ("Times New Roman", 10) , 150, 60)
        #clean writing
        Create_label(deleteDoctorWindow,"Done!" ,("Times New Roman", 10) , 150, 60)
    else:
        Create_label(deleteDoctorWindow,"Not Found!" ,("Times New Roman", 10) , 150, 60)

def editDoctorFunc():
    global doctorID
    if checkIfExist(doctorID.get(),"doctorsRecords.xlsx",0) :
        index = returnRowNum(doctorID.get(),"doctorsRecords.xlsx")
        oldData = []

        # Give the location of the file
        loc = ("doctorsRecords.xlsx")
 
        # To open Workbook
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        
        col = 0
        while col < 5 :
            oldData.append(sheet.cell_value(index, col))
            col += 1

        #delete old data from fileSystem
        deleteEntry(doctorID.get(),"doctorsRecords.xlsx",5)

        #clear data in holdPatientData dict
        holdDoctorData.clear()

        global headings
            
        row = 90
        i = 0
        for heading in headings :
            Create_label(editDoctorWindow,heading + " : " ,("Times New Roman", 10) , 10, row)
            x , z = Create_Entry(editDoctorWindow , 25 , 110 ,row)
            holdDoctorData.append(x)
            x.set(oldData[i])
            row += 20
            i += 1
        
        Create_button(editDoctorWindow, 15 , "Submit" , addDoctorFunc
                  , ("Times New Roman", 10) , 10 , 300)
               
    else:
        Create_label(editDoctorWindow,"Not Found!" ,("Times New Roman", 10) , 150, 60)

def displayDoctorFunc():
    global doctorID
    if checkIfExist(doctorID.get(),"doctorsRecords.xlsx",0) :
        global headings
        printRow(displayDoctorWindow,returnRowNum(doctorID.get(),"doctorsRecords.xlsx"),
                 "doctorsRecords.xlsx", headings, 5)
    else:
        Create_label(displayDoctorWindow,"Not Found!" ,("Times New Roman", 10) , 150, 60)

###########################################################################

def retriveAdminFromAdd():
    global holdy
    global addDoctorWindow
    holdy.deiconify()
    addDoctorWindow.destroy()
    
def retriveAdminFromEdit():
    global holdy
    global editDoctorWindow
    holdy.deiconify()
    editDoctorWindow.destroy()
    
def retriveAdminFromDelete():
    global holdy
    global deleteDoctorWindow
    holdy.deiconify()
    deleteDoctorWindow.destroy()
    
def retriveAdminFromDisplay():
    global holdy
    global displayDoctorWindow
    holdy.deiconify()
    displayDoctorWindow.destroy()
    
def retriveAdminFromDisplayAll():
    global holdy
    global displayAllDoctorWindow
    holdy.deiconify()
    displayAllDoctorWindow.destroy()
