import os
from tkinter import *


os.system("cls")

def main():

    symbols = ['+','-','*','.']

    stage = Tk()
    stage.title("Calculator")
    stage.resizable(width=False,height=False)
    stage.geometry("210x210")

    entery_frame = Frame(stage)
    entery_frame.pack()
    global expression_ 
    expression_ = StringVar()
    entery = Entry(entery_frame,textvariable= expression_)
    entery.pack()


    grid_frame = Frame(stage)
    grid_frame.pack()

   
#############################################################################
    button7 = Button(grid_frame,text='7',width=3,height=2,command= lambda: enter('7'))
    button7.grid(column=0,row=1)

    button8 = Button(grid_frame,text='8',width=3,height=2,command= lambda: enter('8'))
    button8.grid(column=1,row=1)

    button9 = Button(grid_frame,text='9',width=3,height=2,command= lambda: enter('9'))
    button9.grid(column=2,row=1)

    button_devide = Button(grid_frame,text='/',width=3,height=2,command= lambda: enter('/') if len(expression_.get())> 0 and not((expression_.get()[-1] in symbols)) else ...)
    button_devide.grid(column=3,row=1)

#############################################################################
    button4 = Button(grid_frame,text='4',width=3,height=2,command= lambda: enter('4'))
    button4.grid(column=0,row=2)

    button5 = Button(grid_frame,text='5',width=3,height=2,command= lambda: enter('5'))
    button5.grid(column=1,row=2)

    button6 = Button(grid_frame,text='6',width=3,height=2,command= lambda: enter('6'))
    button6.grid(column=2,row=2)

    button_multiply = Button(grid_frame,text='*',width=3,height=2,command= lambda: enter('*') if len(expression_.get())> 0 and not((expression_.get()[-1] in symbols)) else ...)
    button_multiply.grid(column=3,row=2)

#############################################################################
    button1 = Button(grid_frame,text='1',width=3,height=2,command= lambda: enter('1'))
    button1.grid(column=0,row=3)

    button2 = Button(grid_frame,text='2',width=3,height=2,command= lambda: enter('2'))
    button2.grid(column=1,row=3)

    button3 = Button(grid_frame,text='3',width=3,height=2,command= lambda: enter('3'))
    button3.grid(column=2,row=3)

    button_minus = Button(grid_frame,text='-',width=3,height=2,command= lambda: enter('-') if len(expression_.get())> 0 and not((expression_.get()[-1] in symbols)) else ...)
    button_minus.grid(column=3,row=3)

#############################################################################
    button0 = Button(grid_frame,text='0',width=3,height=2,command= lambda: enter('0'))
    button0.grid(column=0,row=4)

    button_coma = Button(grid_frame,text='.',width=3,height=2,command= lambda: enter('.'))
    button_coma.grid(column=1,row=4)

    button_equal = Button(grid_frame,text='=',width=3,height=2,command= calculate)
    button_equal.grid(column=2,row=4)

    button_add = Button(grid_frame,text='+',width=3,height=2,command= lambda: enter('+') if len(expression_.get())> 0  and not((expression_.get()[-1] in symbols)) else ...)
    button_add.grid(column=3,row=4)

    clear_frame = Frame(stage)
    clear_frame.pack()

    button_clear = Button(clear_frame,text="Clear",command=clear,width=16)
    button_clear.pack()
    
    grid_frame.mainloop()




def clear():
    global expression_
    expression_.set("")    

def calculate():

    global expression_

    symbols = ['+','-','*','.']
    if (len(expression_.get())>0) and (expression_.get()[-1] in symbols):

        pass
    else:
        try:
            results = eval(expression_.get())
        except:
            clear()
        else:
            expression_.set(results)

def enter(string):

    global expression_
    expression_.set(expression_.get()+string)


if __name__ == "__main__":
    main()
    
