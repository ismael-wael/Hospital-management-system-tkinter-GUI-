from tkinter import *
import tkinter as tk 
from tkinter import ttk
from GUI_Functions import *
from managePatients import *
from manageDoctors import *
from manageBooking import *

def adminMode(mainWindow_Copy):
    global holdMainWindow
    holdMainWindow = mainWindow_Copy
    global adminWindow
    adminWindow = Toplevel()
    adminWindow.geometry("320x300+1000+100")
    adminWindow.title("Admin")
    mainWindow_Copy.withdraw()
    adminWindow.protocol("WM_DELETE_WINDOW",closeWindow)

    Create_button(adminWindow, 15 , 'Manage Patients'
                  , managePatientfunc , ("Times New Roman", 15) , 80 , 20)
    Create_button(adminWindow, 15 , 'Manage Doctors'
                  , manageDocotorsfunc , ("Times New Roman", 15) , 80 , 70)
    Create_button(adminWindow, 15 , 'Book Appointment'
                  , bookAnApointmentfunc , ("Times New Roman", 15) , 80 , 120)
    
###############################################################################
    
def managePatientfunc():
    #clean last writings
    Create_label(adminWindow,"                                                         " ,
                 ("Times New Roman", 10) , 30, 190)
    #clean writings
    Create_label(adminWindow,"Manage Patients :" , ("Times New Roman", 10) , 30, 190)
    global mPatients
    managePatients = [' Add patient', ' delete patient', ' edit patient',
                      ' display patient' , ' show all patients']
    mPatients , z = Create_Combobox(adminWindow , managePatients , 20 , 150 , 190)
    Create_button(adminWindow, 15 ,'Submit' ,patients ,("Times New Roman", 15) , 40 , 220)

def manageDocotorsfunc():
    #clean last writings
    Create_label(adminWindow,"                                                           " ,
                 ("Times New Roman", 10) , 30, 190)
    #clean writings
    Create_label(adminWindow,"Manage Doctors :" ,("Times New Roman", 10) , 30, 190)  
    global mDoctors
    manageDoctors = [' Add doctor', ' delete doctor', ' edit doctor', ' display dotor',
                     ' show all doctors']
    mDoctors ,z= Create_Combobox(adminWindow ,manageDoctors ,20 ,150 ,190)
    Create_button(adminWindow ,15 ,'Submit' ,doctors ,("Times New Roman", 15) ,40 ,220)

def bookAnApointmentfunc():
    #clean last writings
    Create_label(adminWindow,"                                                            " ,
                 ("Times New Roman", 10) , 30, 190)
    #clean writings
    Create_label(adminWindow,"Book Appointment :" ,("Times New Roman", 10) , 30, 190)
    global bAppointment
    bookAppointments = [' book appointment', ' edit appointment',
                        ' cancel appointment',' display appointment']
    bAppointment , z = Create_Combobox(adminWindow , bookAppointments , 20 , 150 , 190)
    Create_button(adminWindow, 15 ,'Submit' , booking , ("Times New Roman", 15) , 40 , 220)
    
########################################################################
def patients():
    n = mPatients.get()
    if(n == ' Add patient'):
        addPatient(adminWindow)
    elif (n == ' delete patient'):
        deletePatient(adminWindow)
    elif (n == ' edit patient'):
        editPatient(adminWindow)
    elif (n == ' display patient'):
        displayPatient(adminWindow)
    elif (n == ' show all patients'):
        displayAllPatient(adminWindow)
        
def doctors():
    n = mDoctors.get()
    if(n == ' Add doctor'):
        addDoctor(adminWindow)
    elif (n == ' delete doctor'):
        deleteDoctor(adminWindow)
    elif (n == ' edit doctor'):
        editDoctor(adminWindow)
    elif (n == ' display dotor'):
        displayDoctor(adminWindow)
    elif (n == ' show all doctors'):
        displayAllDoctor(adminWindow)
        
def booking():
    n = bAppointment.get()
    if(n == ' book appointment'):
        bookAppointment(adminWindow)
    elif (n == ' edit appointment'):
        editAppointment(adminWindow)
    elif (n == ' cancel appointment'):
        cancelAppointment(adminWindow)
    elif (n == ' display appointment'):
        displayAppointment(adminWindow)
#################################################################################

def closeWindow():
    global holdMainWindow
    global adminWindow
    holdMainWindow.deiconify()
    adminWindow.destroy()
