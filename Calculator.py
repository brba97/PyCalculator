from tkinter import *


calc = Tk()
calc.title("CALCULATOR")

display = Entry(calc, width=64)        # white display
display.grid(row=0, column=0, columnspan=12, pady=20)


def buttons(val):     # insert value of buttons into display
    display.insert(END, val)


n1 = Button(calc, width=8, height=4, text='  1  ', command=lambda: buttons(1))
n1.grid(row=2, column=0)
n2 = Button(calc, width=8, height=4, text='  2  ', command=lambda: buttons(2))
n2.grid(row=2, column=2)
n3 = Button(calc, width=8, height=4, text='  3  ', command=lambda: buttons(3))
n3.grid(row=2, column=4)
n4 = Button(calc, width=8, height=4, text='  4  ', command=lambda: buttons(4))
n4.grid(row=4, column=0)
n5 = Button(calc, width=8, height=4, text='  5  ', command=lambda: buttons(5))
n5.grid(row=4, column=2)
n6 = Button(calc, width=8, height=4, text='  6  ', command=lambda: buttons(6))
n6.grid(row=4, column=4)
n7 = Button(calc, width=8, height=4, text='  7  ', command=lambda:buttons(7))
n7.grid(row=6, column=0)
n8 = Button(calc, width=8, height=4, text='  8  ', command=lambda:buttons(8))
n8.grid(row=6, column=2)
n9 = Button(calc, width=8, height=4, text='  9  ', command=lambda:buttons(9))
n9.grid(row=6, column=4)
n10 = Button(calc, width=8, height=4, text='  0  ', command=lambda: buttons(0))
n10.grid(row=8, column=2)
n11 = Button(calc, width=8, height=4, text='Pow', command=lambda: buttons('pow'))
n11.grid(row=8, column=4, columnspan=2)
op1 = Button(calc, width=8, height=4, text='  /  ', command=lambda: buttons('/'))
op1.grid(row=2, column=6)
op2 = Button(calc, width=8, height=4, text='  *  ', command=lambda: buttons('*'))
op2.grid(row=4, column=6)
op3 = Button(calc, width=8, height=4, text='  %  ', command=lambda: buttons('%'))
op3.grid(row=6, column=6)
op4 = Button(calc, width=8, height=4, text='  +  ', command=lambda: buttons('+'))
op4.grid(row=2, column=8)
op5 = Button(calc, width=8, height=4, text='  .  ', command=lambda: buttons('.'))
op5.grid(row=8, column=0)
op6 = Button(calc, width=8, height=4, text='  CLR  ', command=lambda: display.delete(0, END))        # clear the display
op6.grid(row=2, column=10)
op7 = Button(calc, width=8, height=4, text='  CE  ', command=lambda: display.delete(len(display.get())-1, END))     # remove last input on display
op7.grid(row=4, column=10)
op8 = Button(calc, width=8, height=4, text='  (  ', command=lambda: buttons('('))
op8.grid(row=8, column=6)
op9 = Button(calc, width=8, height=4, text='  )  ', command=lambda: buttons(')'))
op9.grid(row=8, column=8)
op10 = Button(calc, width=8, height=4, text='  ,  ', command=lambda: buttons(','))
op10.grid(row=6, column=10)
op11 = Button(calc, width=8, height=4, text='  -  ', command=lambda: buttons('/'))
op11.grid(row=4, column=8)


def equals(exprsn):      # function for '='
    try:
        value = eval(exprsn.get())

    except SyntaxError or NameError:
        exprsn.delete(0, END)
        exprsn.insert(0, 'unsupported expression')
    else:
        exprsn.delete(0, END)
        exprsn.insert(0, value)


eq = Button(calc, width=8, height=4, text='  =  ', command=lambda: equals(display))
eq.grid(row=6, column=8)
lb = Label(calc, width=8, height=4, text='pow(4,1/2)\n=4^0.5\n=2.0')
lb.grid(row=8, column=10)

calc.mainloop()

