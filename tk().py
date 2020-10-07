from tkinter import*
def assignNum(num):

    global operator
    operator= operator + str(num)
    userInput.set(operator)

def clean():

    global operator
    operator= ''
    userInput.set(operator)

def Equal():

    global operator
    numEval = str(eval(operator))
    userInput.set(numEval)
    operator= ''

calc = Tk()
calc.title("SIMPLE CALCULATOR")
userInput = StringVar()
operator = ''
textInput= Entry(calc, font= ('arial', 20, 'bold'), textvariable= '', bd= 30, bg= 'magenta', justify= 'left').grid(columnspan= 4)

btnClear= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='C', command= lambda:clean()).grid(row= 1, column= 0)
btnPower= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='^', command= lambda:assignNum('**')).grid(row= 1, column= 1)
btnPerc= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='%', command= lambda:assignNum('%')).grid(row= 1, column= 2)
btnDiv= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='/', command= lambda:assignNum('/')).grid(row= 1, column= 3)

btn7= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='7', command= lambda:assignNum(7)).grid(row= 2, column= 0)
btn8= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='8', command= lambda:assignNum(8)).grid(row= 2, column= 1)
btn9= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='9', command= lambda:assignNum(9)).grid(row= 2, column= 2)
btnMulti= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='*', command= lambda:assignNum('*')).grid(row= 2, column= 3)

btn4= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='4', command= lambda:assignNum(4)).grid(row= 3, column= 0)
btn5= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='5', command= lambda:assignNum(5)).grid(row= 3, column= 1)
btn6= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='6', command= lambda:assignNum(6)).grid(row= 3, column= 2)
btnMinus= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='-', command= lambda:assignNum('-')).grid(row= 3, column= 3)

btn1= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='1', command=lambda:assignNum(1)).grid(row= 4, column= 0)
btn2= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='2', command=lambda:assignNum(2)).grid(row= 4, column= 1)
btn3= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='3', command=lambda:assignNum(3)).grid(row= 4, column= 2)
btnAdd= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='+', command=lambda:assignNum('+')).grid(row= 4, column= 3)


btn0= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='0', command=lambda:assignNum(0)).grid(row= 5, column= 0)
btnComma= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='.', command=lambda:assignNum('.')).grid(row= 5, column= 1)
btnEqual= Button(calc, padx= 16, bd= 8, fg= 'cyan', font=('arial',20, 'bold'), text='=', command=lambda:assignNum('=')).grid(row= 5, column= 2)

calc.mainloop()