# ******************************************************************************
# Author:           Noah McGarry
# Lab:              Lab 9
# Date:             8/23/2023
# Description:      Lab 9 Program
#
# Input:            name, string, name of person to search database for
#                   gender, string, M or F for gender to search database for
#
# Output:           Results from pymssql Names database
#
# Sources:          Lab 9 specifications
#
#
# Comments:         I had fun with this one, hopefully this does everything
#                   it needs to do. I didn't use the pygubu since you mentioned
#                   in the lecture video that we didn't need to. I think the
#                   GUI looks fine without it.
#
# ******************************************************************************


#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from Names import Names


def click_button1():
    """
    Retrieves list from getNames function according to name and gender choice entered
    from Names.py and prints to GUI and console.
    :return: none
    """
    print(strName.get(), strGender.get())
    name = strName.get()
    gender = strGender.get()
    namesList = []
    namesList = Names.getNames(name, gender)

    for c in namesList:
        entry = (c.name, c.gender, c.year, c.births)
        print()
        print(c)
        censuslist.insert('', tk.END, values=entry)


def click_button2():
    """
    Prints to console and exits program
    :return: none
    """
    print("OH NO!")
    root.destroy()


root = tk.Tk()
root.title("Noah's Amazing Magical GUI Census Program")
root.geometry("820x330")

strName = tk.StringVar()
strGender = tk.StringVar()

frmOne = ttk.Frame(root, padding="10 10 10 10")
frmOne.pack(fill=tk.BOTH, expand=True)

lblName = ttk.Label(frmOne, text="Please enter a Name:")
lblName.grid(column=0, row=0, sticky=tk.W)

txtName = ttk.Entry(frmOne, width=18, textvariable=strName)
strName.set("Noah")
txtName.grid(column=0, row=0, sticky=tk.E)

lblGender = ttk.Label(frmOne, text="Enter a Gender (M/F):")
lblGender.grid(column=0, row=1, sticky=tk.W)

txtGender = ttk.Entry(frmOne, width=2, textvariable=strGender)
strGender.set("M")
txtGender.grid(column=0, row=1, sticky=tk.E)

button1 = ttk.Button(frmOne, text="Click ME!", command=click_button1)
button2 = ttk.Button(frmOne, text="DON'T CLICK ME! (EXIT)", command=click_button2)

button1.grid(column=0, row=2, sticky=tk.W)
button2.grid(column=0, row=2, sticky=tk.E)

columns = ('Name', 'Gender', 'Year', 'Births')
censuslist = ttk.Treeview(frmOne, columns=columns, show='headings')

censuslist.heading('Name', text='Name')
censuslist.heading('Gender', text='Gender')
censuslist.heading('Year', text='Year')
censuslist.heading('Births', text='Births')
censuslist.grid(column=0, row=3, sticky=tk.W)

root.mainloop()