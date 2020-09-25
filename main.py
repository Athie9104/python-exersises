# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:27:51 2019

@author: stud6
"""
from tkinter import *
#from Logic.py import *


def main():
    #depObj = Transaction()
    # depObj.option()
    mF = Tk()

    mF.minsize(width=200, height=150)
    mF.maxsize(width=300, height=200)
    Label(mF, fg='red', text='ATM PROJECT', font=('berlin sans fb demi', 20, 'underline',)).pack()
    Label(mF, text='Choose Option', font=('berlin sans fb demi', 20, 'underline',)).pack()

    '''Button(mF, text='Deposit', fg='cyan', bg='green', font=('berlin sans fb', 14),
           command=lambda: depObj.option()).pack()'''
    Button(mF, text='Withdrawal', fg='cyan', bg='orange', font=('berlin sans fb', 14)).pack()
    Button(mF, text='Enquiry', fg='cyan', bg='yellow', font=('berlin sans fb', 14)).pack()

    mF.mainloop()
