from tkinter import *
from typing import get_args

win=Tk()
win.title("Calculator")
win.geometry("570x600+100+200")
win.resizable(False,False)
win.configure(bg='grey')


label_result=Label(win,width=25,height=2,text="",background='red',font=('arial',30)) #for output screen
label_result.pack()

eqn=""
def disp(val):
    global eq
    eqn+=val
    label_result.config(text=eqn)

def clear():
    global eqn
    eqn=""
    label_result.config(text=eqn)

def calculate():
    global eqn 
    result=""
    if eqn !="":
        try:
            result=eval(eqn)
        except:
            result="error"
            eqn=""
    label_result.config(text=result)
    # what was the point.

Button(win,text='C',width=5,height=1,font=('arial',30),command=lambda: clear()).place(x=10,y=100)
Button(win,text='/',width=5,height=1,font=('arial',30),command=lambda: disp('/')).place(x=150,y=100)
Button(win,text='*',width=5,height=1,font=('arial',30),command=lambda: disp('*')).place(x=290,y=100)
Button(win,text='+',width=5,height=1,font=('arial',30),command=lambda: disp('+')).place(x=430,y=100)

Button(win,text='-',width=5,height=1,font=('arial',30),command=lambda: disp('-')).place(x=10,y=200)
Button(win,text='0',width=5,height=1,font=('arial',30),command=lambda: disp('0')).place(x=150,y=200)
Button(win,text='1',width=5,height=1,font=('arial',30),command=lambda: disp('1')).place(x=290,y=200)
Button(win,text='2',width=5,height=1,font=('arial',30),command=lambda: disp('2')).place(x=430,y=200)

Button(win,text='3',width=5,height=1,font=('arial',30),command=lambda: disp('3')).place(x=10,y=300)
Button(win,text='4',width=5,height=1,font=('arial',30),command=lambda: disp('4')).place(x=150,y=300)
Button(win,text='5',width=5,height=1,font=('arial',30),command=lambda: disp('5')).place(x=290,y=300)
Button(win,text='6',width=5,height=1,font=('arial',30),command=lambda: disp('6')).place(x=430,y=300)

Button(win,text='7',width=5,height=1,font=('arial',30),command=lambda: disp('7')).place(x=10,y=400)
Button(win,text='8',width=5,height=1,font=('arial',30),command=lambda: disp('8')).place(x=150,y=400)
Button(win,text='9',width=5,height=1,font=('arial',30),command=lambda: disp('9')).place(x=290,y=400)
Button(win,text='=',width=5,height=1,font=('arial',30),background='gold',command=lambda: calculate()).place(x=430,y=400)
win.mainloop()
