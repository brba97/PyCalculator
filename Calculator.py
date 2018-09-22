from tkinter import *
from math import *


calc = Tk()
calc.title("CALCULATOR")
calc.resizable(0, 0)

display = Entry(calc, width=64)        # white display
display.grid(row=0, column=0, columnspan=12, pady=20)


def buttons(val):     # insert value of buttons into display
    display.insert(END, val)

# Numbers:

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

# Math signs:

Ms1 = Button(calc, width=8, height=4, text='  /  ', command=lambda: buttons('/'))
Ms1.grid(row=2, column=6)
Ms2 = Button(calc, width=8, height=4, text='  *  ', command=lambda: buttons('*'))
Ms2.grid(row=4, column=6)
Ms3 = Button(calc, width=8, height=4, text='  %  ', command=lambda: buttons('%'))
Ms3.grid(row=6, column=6)
Ms4 = Button(calc, width=8, height=4, text='  +  ', command=lambda: buttons('+'))
Ms4.grid(row=2, column=8)
Ms5 = Button(calc, width=8, height=4, text='  .  ', command=lambda: buttons('.'))
Ms5.grid(row=8, column=0)
Ms6 = Button(calc, width=8, height=4, text='  (  ', command=lambda: buttons('('))
Ms6.grid(row=8, column=6)
Ms7 = Button(calc, width=8, height=4, text='  )  ', command=lambda: buttons(')'))
Ms7.grid(row=8, column=8)
Ms8 = Button(calc, width=8, height=4, text='  ,  ', command=lambda: buttons(','))
Ms8.grid(row=8, column=4)
Ms9 = Button(calc, width=8, height=4, text='  -  ', command=lambda: buttons('/'))
Ms9.grid(row=4, column=8)


def equals(exprsn):      # function for '='
    try:
        value = eval(exprsn.get())
        exprsn.delete(0, END)
        exprsn.insert(0, value)
        
    except:
        exprsn.delete(0, END)
        exprsn.insert(0, 'unsupported expression')
        

eq = Button(calc, width=8, height=4, text='  =  ', command=lambda: equals(display))
eq.grid(row=6, column=8)

f1 = Button(calc, width=8, height=4, text='Pow', command=lambda: buttons('pow'))
f1.grid(row=6, column=10)
f2 = Button(calc, width=8, height=4, text='Log', command=lambda: buttons('log'))
f2.grid(row=8, column=10)

f3 = Button(calc, width=8, height=4, text='  CLR  ', command=lambda: display.delete(0, END))        # clear the display
f3.grid(row=2, column=10)
f4 = Button(calc, width=8, height=4, text='  CE  ', command=lambda: display.delete(len(display.get())-1, END))     # remove last input on display
f4.grid(row=4, column=10)

calc.mainloop()

