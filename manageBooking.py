from tkinter import *
import tkinter as tk 
from tkinter import ttk
from GUI_Functions import *
import xlsxwriter
import xlrd
from helperFunctions import *

holdBookingData = []

headings = ["Patient ID","Dep. name", "Doctor","Date","Time",
            "Name", "Age", "Gender"]

def bookAppointment(y):
    global holdy
    holdy = y
    global bookAppointmentWindow
    bookAppointmentWindow = Toplevel()
    bookAppointmentWindow.geometry("320x300+1000+100")
    bookAppointmentWindow.title("Book Appointment")
    
    y.withdraw()
    bookAppointmentWindow.protocol("WM_DELETE_WINDOW",retriveAdminFromBookAppointment)

    global headings 

    #clear old data in holdBookingData
    holdBookingData.clear()
    
    row = 20
    for heading in headings :
        Create_label(bookAppointmentWindow,heading + " : " ,("Times New Roman", 10) , 20, row)
        entry , z = Create_Entry(bookAppointmentWindow , 25 , 110 ,row)
        holdBookingData.append(entry)
        row += 20
        
    Create_button(bookAppointmentWindow, 15 , "Submit" , bookAppointmentFunc
                  , ("Times New Roman", 10) , 20 , 240)

def editAppointment(y):
    global holdy
    holdy = y
    global editAppointmentWindow
    editAppointmentWindow = Toplevel()
    editAppointmentWindow.geometry("320x350+1000+100")
    editAppointmentWindow.title("Edit Appointment")
    y.withdraw()
    editAppointmentWindow.protocol("WM_DELETE_WINDOW",retriveAdminFromEditAppointment)

    Create_label(editAppointmentWindow,"Enter patient ID :" ,("Times New Roman", 10) , 10, 20)

    global patientID
    patientID , z = Create_Entry(editAppointmentWindow , 25 , 120 ,20)    

    Create_button(editAppointmentWindow, 15 , "Submit" , editAppointmentFunc
                  , ("Times New Roman", 10) , 10 , 60)
    
def cancelAppointment(y):
    global holdy
    holdy = y
    global cancelAppointmentWindow
    cancelAppointmentWindow = Toplevel()
    cancelAppointmentWindow.geometry("300x100+1000+100")
    cancelAppointmentWindow.title("Cancel Appointment")
    y.withdraw()
    cancelAppointmentWindow.protocol("WM_DELETE_WINDOW",retriveAdminFromCancelAppointment)

    Create_label(cancelAppointmentWindow,"Enter patient ID :" ,("Times New Roman", 10) , 10, 20)

    global patientID
    patientID , z= Create_Entry(cancelAppointmentWindow , 25 , 120 ,20)    

    Create_button(cancelAppointmentWindow, 15 , "Submit" , cancelAppointmentFunc
                  , ("Times New Roman", 10) , 10 , 60)
    
def displayAppointment(y):
    global holdy
    holdy = y
    global displayAppointmentWindow
    displayAppointmentWindow = Toplevel()
    displayAppointmentWindow.geometry("300x300+1000+100")
    displayAppointmentWindow.title("Display Appointment")
    y.withdraw()
    displayAppointmentWindow.protocol("WM_DELETE_WINDOW",retriveAdminFromDisplayAppointment)

    Create_label(displayAppointmentWindow,"Enter patient ID :" ,("Times New Roman", 10) , 10, 20)

    global patientID
    patientID , z = Create_Entry(displayAppointmentWindow , 25 , 120 ,20)    

    Create_button(displayAppointmentWindow, 15 , "Submit" , displayAppointmetFunc
                  , ("Times New Roman", 10) , 10 , 60)
#######################################################################
def bookAppointmentFunc():
    if(checkIfExist(holdBookingData[0].get(),"bookingRecords.xlsx",0)):#check ID
        Create_label(bookAppointmentWindow,"Reserved ID!",("Times New Roman", 10) , 150, 240)
    elif(checkIfExist(holdBookingData[1].get(),"bookingRecords.xlsx",1) and #department
         checkIfExist(holdBookingData[2].get(),"bookingRecords.xlsx",2) and #doctor
         checkIfExist(holdBookingData[3].get(),"bookingRecords.xlsx",3) and #Date
         checkIfExist(holdBookingData[4].get(),"bookingRecords.xlsx",4)): #Time

        Create_label(bookAppointmentWindow,"Reserved Appointment!",
                     ("Times New Roman", 10) , 150, 240)
        Create_label(bookAppointmentWindow,"(Sorry. choose another date/time.)",
                     ("Times New Roman",10),150,260)
    else :
        newEntry("bookingRecords.xlsx",holdBookingData,8)

def editAppointmentFunc():
    global patientID
    if checkIfExist(patientID.get(),"bookingRecords.xlsx",0) :
        index = returnRowNum(patientID.get(),"bookingRecords.xlsx")
        oldData = []

        # Give the location of the file
        loc = ("bookingRecords.xlsx")
 
        # To open Workbook
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        
        col = 0
        while col < 8 :
            oldData.append(sheet.cell_value(index, col))
            col += 1

        #delete old data from fileSystem
        deleteEntry(patientID.get(),"bookingRecords.xlsx",8)

        #clear data in holdPatientData dict
        holdBookingData.clear()

        global headings
            
        row = 90
        i = 0
        for heading in headings :
            Create_label(editAppointmentWindow,heading + " : " ,("Times New Roman", 10) , 10, row)
            x , z= Create_Entry(editAppointmentWindow , 25 , 110 ,row)
            holdBookingData.append(x)
            x.set(oldData[i])
            row += 20
            i += 1
        
        Create_button(editAppointmentWindow, 15 , "Submit" , bookAppointmentFunc
                  , ("Times New Roman", 10) , 10 , 300)
               
    else:
        Create_label(editAppointmentWindow,"Not Found!" ,("Times New Roman", 10) , 150, 60)

def cancelAppointmentFunc():
    global patientID
    if checkIfExist(patientID.get(),"bookingRecords.xlsx",0) :
        deleteEntry(patientID.get(),"bookingRecords.xlsx",8)
        #clear last writings here ("Not Found!")
        Create_label(cancelAppointmentWindow,"                                " ,
                     ("Times New Roman", 10) , 150, 60)
        #clean writing
        Create_label(cancelAppointmentWindow,"Done!" ,("Times New Roman", 10) , 150, 60)
    else:
        Create_label(cancelAppointmentWindow,"Not Found!" ,("Times New Roman", 10) , 150, 60)

def displayAppointmetFunc():
    global patientID
    if checkIfExist(patientID.get(),"bookingRecords.xlsx",0) :
        global headings
        printRow(displayAppointmentWindow ,returnRowNum(patientID.get(),"bookingRecords.xlsx")
                     ,"bookingRecords.xlsx",headings,8)
    else:
        Create_label(displayAppointmentWindow,"Not Found!" ,("Times New Roman", 10) , 150, 60)

#######################################################################

def retriveAdminFromBookAppointment():
    global holdy
    global bookAppointmentWindow
    holdy.deiconify()
    bookAppointmentWindow.destroy()

def retriveAdminFromCancelAppointment():
    global holdy
    global cancelAppointmentWindow
    holdy.deiconify()
    cancelAppointmentWindow.destroy()

def retriveAdminFromEditAppointment():
    global holdy
    global editAppointmentWindow
    holdy.deiconify()
    editAppointmentWindow.destroy()

def retriveAdminFromDisplayAppointment():
    global holdy
    global displayAppointmentWindow
    holdy.deiconify()
    displayAppointmentWindow.destroy()

#############################################################################



    
