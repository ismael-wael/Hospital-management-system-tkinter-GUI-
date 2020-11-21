from tkinter import *
import tkinter as tk

def Create_label(window,txt , fnt , x1, y1):
    label = Label(window,text=txt,font=fnt)
    label.place (x = x1 , y = y1)
    return label

def Create_button(window, wdth , txt , cmd , fnt , x1 , y1):
    button = Button(window,width = wdth,text=txt,
                 command=cmd,font = fnt)
    button.place(x = x1 , y = y1)
    return button

def Create_Entry(window , wdth , x1 ,y1):
    variable = tk.StringVar()
    entry = Entry(window , width = wdth , textvariable = variable)
    entry.place(x = x1, y = y1)
    return variable , entry

def Create_Combobox(window , vals , wdth , x1 , y1):
    variable = tk.StringVar()
    combobox = ttk.Combobox(window,values = vals
                            ,width = wdth, textvariable = variable)
    combobox.current()
    combobox.place(x = x1, y = y1)
    return variable , combobox

def CreateTextScrollbar(window , height_ , width_):
    Scroll = tk.Scrollbar(window)
    Text = tk.Text(window, height=height_, width=width_)
    Scroll.pack(side=tk.RIGHT, fill=tk.Y)
    Text.pack(side=tk.LEFT, fill=tk.Y)
    Scroll.config(command=Text.yview)
    Text.config(yscrollcommand=Scroll.set)
    return Text

