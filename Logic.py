# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:00:15 2019

@author: stud6
"""
from tkinter import *


class Transaction:
    @staticmethod
    def option():
        dep = Tk()
        dep.minsize(width=200, height=150)
        dep.maxsize(width=300, height=200)

        Radiobutton(dep, fg='red', text='100', value=0, font=('berlin sans fb demi', 20, 'underline',)).grid(row=0,
                                                                                                             column=0)
        Radiobutton(dep, fg='green', text='500', value=1, font=('berlin sans fb demi', 20, 'underline',)).grid(row=1,
                                                                                                               column=0)
        Radiobutton(dep, fg='orange', text='1000', value=2, font=('berlin sans fb demi', 20, 'underline',)).grid(row=2,
                                                                                                                 column=0)

        Radiobutton(dep, fg='blue', text='5000', value=3, font=('berlin sans fb demi', 20, 'underline',)).grid(row=0,
                                                                                                               column=1)
        Radiobutton(dep, fg='yellow', text='10000', value=4, font=('berlin sans fb demi', 20, 'underline',)).grid(row=1,
                                                                                                                  column=1)
        Radiobutton(dep, fg='cyan', text='15000', value=5, font=('berlin sans fb demi', 20, 'underline',)).grid(row=2,
                                                                                                                column=1)

        dep.mainloop()
# o = Transaction()
# o.option()