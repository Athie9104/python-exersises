# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 09:40:14 2019

@author: stud6
"""

from tkinter import *
#from main.py import *


def logInOth():
    pNum = inputPin.get()
    pinLst = {'Athi': '1234', 'Thabo': '4321', 'Mpumei': '5678'}

    for x in pinLst.values():
        if x == pNum:
            pin.destroy()
            #main.py()
        elif x != pNum:
            clean()


def clean():
    global operator
    operator = ''
    inputPin.set(operator)


pin = Tk()
inputPin = StringVar()
operator = ''

pin.minsize(width=350, height=200)
pin.maxsize(width=350, height=200)
pin.title('Pin Number Form')
Label(pin, text='ATM PROJECT', font=('berlin sans fb demi', 20, 'underline',)).grid(columnspan=2)
Label(pin, text='Enter Pin Number In Field Below:', font=('berlin sans fb', 19, 'underline',)).grid(columnspan=2)
Label(pin, pady=30, text='Pin Number', font=('berlin sans fb', 14)).grid(row=2, column=0)

Entry(pin, textvariable=inputPin, font=('berlin sans fb', 14)).grid(row=2, column=1)

Button(pin, text='Enter', fg='green', bg='Yellow', font=('berlin sans fb', 14), command=lambda: logInOth()).grid(row=3,
                                                                                                               column=0)
Button(pin, text='Refresh', fg='white', bg='red', font=('berlin sans fb', 14), command=lambda: clean()).grid(row=3,
                                                                                                             column=1)

pin.mainloop()