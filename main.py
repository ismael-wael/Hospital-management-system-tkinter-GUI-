from tkinter import *
import tkinter as tk 
from tkinter import ttk
from GUI_Functions import *
from admin import *
from managePatients import *
from manageDoctors import *
from manageBooking import *

global password
global username
global username_label
global password_label
global password_entry
global username_entry
global button
global select
global comboBox
global userButton

global user_flag
user_flag = 0

global admin_flg
admin_flag = 0

#########################################################################################
def createMainWindow():
    global MainWindow
    MainWindow = Tk()
    MainWindow.geometry("320x300+1000+100")
    MainWindow.title("Hospital Project")
    
    Create_label(MainWindow,'Choose Mode :' , ("Times New Roman", 20) , 80, 20)
    Create_button(MainWindow, 15 , 'Admin' , admin , ("Times New Roman", 15) , 80 , 90)
    Create_button(MainWindow, 15 , 'User' , user , ("Times New Roman", 15) , 80 , 140)
    
    MainWindow.mainloop()

#########################################################################################    
def admin():
    
    
    global password
    global username
    global username_label
    global password_label
    global password_entry
    global username_entry
    global button
    global select
    global comboBox
    global userButton
    global user_flag
    global admin_flag

    admin_flag = 1

    if (user_flag == 1):
        select.destroy()
        comboBox.destroy()
        userButton.destroy()

    username_label = Create_label(MainWindow,"Username" , ("Times New Roman", 10) , 20, 190)
    password_label= Create_label(MainWindow,"Password" , ("Times New Roman", 10) , 20, 230)
    username , username_entry = Create_Entry(MainWindow , 15 , 90 ,190)
    password , password_entry = Create_Entry(MainWindow , 15 , 90 ,230)
    button = Create_button(MainWindow, 15 , "Submit" , submit , ("Times New Roman", 10) , 20 , 260)

def submit():
    global password
    
    if str(password.get()) == "1234":
        adminMode(MainWindow)
    elif submit.count == 3:
        MainWindow.destroy()
    else:
        submit.count += 1
submit.count = 1

#########################################################################################
def user():

    global password
    global username
    global username_label
    global password_label
    global password_entry
    global username_entry
    global button
    global select
    global comboBox
    global userButton
    global user_flag
    global admin_flag

    user_flag = 1

    if (admin_flag == 1):
        username_label.destroy()
        password_label.destroy()
        username_entry.destroy()
        password_entry.destroy()
        button.destroy()

    select = Create_label(MainWindow,"Select :" , ("Times New Roman", 15) , 50, 190)
    global userChoice
    options = [' View All Departments', ' View All Doctors', ' View All Patients',
                      ' View Patient' , ' View Appointment']
    userChoice , comboBox = Create_Combobox(MainWindow , options , 20 , 130 , 190)
    userButton = Create_button(MainWindow, 7,'Submit',userChoiceFunc ,("Times New Roman", 15) , 40 , 220)

def userChoiceFunc():
    m = userChoice.get()
    if(m == ' View All Departments'):
        displayAllDepartments()
    elif (m == ' View All Doctors'):
        displayAllDoctor(MainWindow)
    elif (m == ' View All Patients'):
        displayAllPatient(MainWindow)
    elif (m == ' View Patient'):
        displayPatient(MainWindow)
    elif (m == ' View Appointment'):
        displayAppointment(MainWindow)

def displayAllDepartments():
    global displayAllDepartmentsWindow
    displayAllDepartmentsWindow = Toplevel()
    displayAllDepartmentsWindow.geometry("350x300+1000+100")
    displayAllDepartmentsWindow.title("All Departments")
    MainWindow.withdraw()
    displayAllDepartmentsWindow.protocol("WM_DELETE_WINDOW"
                                         ,retriveMainFromDisplayAllDepartments)
    
    text = CreateTextScrollbar(displayAllDepartmentsWindow , 350 , 300)
    
    departments = ['Surgery' , 'Vascular Surgery' , 'Cardiovascular Internal Medicine',
                   'Orthopedic Surgery' , 'Cranial Nerve Internal Medicine',
                   'Neurosurgery', 'Mammary Gland Surgery', 'Endoscopic Internal Medicine',
                   'Pediatrics', 'Internal Medicine', 'Rehabilitation',
                   'Reconstructive and Cosmetic Surgery']
    num = 1
    for i in departments :
            text.insert("end",str(num) + ' - '+ i + ".")
            text.insert("end", '\n\n')
            num += 1
    text.insert("end", '******************************\n')

def retriveMainFromDisplayAllDepartments():
    global displayAllDepartmentsWindow
    MainWindow.deiconify()
    displayAllDepartmentsWindow.destroy()

#########################################################################################

createMainWindow()



    

