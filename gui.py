# from tkinter import *   # this is used for GUI options.
# win = Tk()

# win.mainloop()
# win.title("Goodbye World!")             # creating an object of Tk class
# win.geometry("300x300")

# ll = Label(win, text = "Enter a")       # creating an object of Label class
# ll.pack(padx=10, pady=10)                                # will display everything.


# e1 = Entry(win, text= "Enter the value of a: ")
# e1.pack()
# e2 = Entry(win, text= "Enter the value of b: ")
# e2.pack()

# def add(): 
#     a = e1.get()
#     b = e2.get()
    

# Button(win, text = "Add", command = add).pack()
# result_label = Label(win, text = "Result: ")
# result_label.pack()



# Tk.pack()
# win.mainloop()
from tkinter import * # this is used for GUI options.

#creating the main windows object.
win = Tk()  # this is the object of the class Tk
win.title('Wick is here')
win.geometry('300x300')
# label is used to display information to the user.
ll = Label(win, text = "Hey, Wick is here!") # creating an object of label class
ll.pack(padx = 10, pady = 10)

#function to add the variables and display the result
def add():
    a = e1.get() # getting the value from the first Entry widget.
    b = d1.get() # getting the value from the second Entry widget.
    try : 
        result = float(a) + float(b)
        result_label.config(text = f"Result : {result}") 
    except ValueError:
        result_label.config(text = "Please enter a valid number!")
        


#creating and placing Entry widget , taking the values of the user.
e = Label(win, text = "Enter the value of a: ")
e.pack()
e1 = Entry(win) 
e1.pack()

d= Label(win, text = "Enter the value of b: ")
d.pack()
d1 = Entry(win) 
d1.pack()

Button(win, text = 'Add', command = add).pack(padx = 10, pady = 10) # button to trigger the add function and display the result.

result_label = Label(win) # creating an object of label class for result.
result_label.pack(padx = 10, pady = 10)
win.mainloop()