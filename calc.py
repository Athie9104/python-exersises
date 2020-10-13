
# Athenkosi Gongotha
from tkinter import *


def assignNum(num):
    global operator
    operator = operator + str(num)
    userInput.set(operator)


def clean():
    global operator
    operator = ''
    userInput.set(operator)


def Equal():
    global operator
    numEval = str(eval(operator))
    userInput.set(numEval)
    operator = ''


calc = Tk()
calc.title('Simple Calculator')
userInput = StringVar()
operator = ''
textInput = Entry(calc, font=('arial', 20, 'bold'), textvariable=userInput, bd=30, bg='cadet blue',
                  justify='right').grid(columnspan=4)

btnClear = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), bg='cadet blue', text='c',
                  command=lambda: clean()).grid(row=1, column=0)
btnPower = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), bg='cadet blue', text='^',
                  command=lambda: assignNum('**')).grid(row=1, column=1)
btnPerc = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='%', bg='cadet blue',
                 command=lambda: assignNum('%')).grid(row=1, column=2)
btnDiv = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='/', bg='cadet blue',
                command=lambda: assignNum('/')).grid(row=1, column=3)

btnSeven = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='7', bg='cadet blue',
                  command=lambda: assignNum(7)).grid(row=2, column=0)
btnEight = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='8', bg='cadet blue',
                  command=lambda: assignNum(8)).grid(row=2, column=1)
btnNine = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='9', bg='cadet blue',
                 command=lambda: assignNum(9)).grid(row=2, column=2)
btnMult = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold',), text='*', bg='cadet blue',
                 command=lambda: assignNum('*')).grid(row=2, column=3)

btnFour = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='4', bg='cadet blue',
                 command=lambda: assignNum(4)).grid(row=3, column=0)
btnFive = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='5', bg='cadet blue',
                 command=lambda: assignNum(5)).grid(row=3, column=1)
btnSix = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='6', bg='cadet blue',
                command=lambda: assignNum(6)).grid(row=3, column=2)
btnMinus = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='-', bg='cadet blue',
                  command=lambda: assignNum('-')).grid(row=3, column=3)

btnOne = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='1', bg='cadet blue',
                command=lambda: assignNum(1)).grid(row=4, column=0)
btnTwo = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='2', bg='cadet blue',
                command=lambda: assignNum(2)).grid(row=4, column=1)
btnThree = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='3', bg='cadet blue',
                  command=lambda: assignNum(3)).grid(row=4, column=2)
btnPlus = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='+', bg='cadet blue',
                 command=lambda: assignNum('+')).grid(row=4, column=3)

btnZero = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='0', bg='cadet blue',
                 command=lambda: assignNum(0)).grid(row=5, column=0)
btnFull = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='.', bg='cadet blue',
                 command=lambda: assignNum('.')).grid(row=5, column=1)
btnEqual = Button(calc, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='=', bg='cadet blue',
                  command=lambda: Equal()).grid(row=5, column=2)

calc.mainloop()
'''
calculator.txt
Displaying
calculator.txt.'''