from cgitb import text
from tkinter import *
#We call the file GUI_main python script into our GUI interface so we can solve our ODEs.
import GUI_main as mn
#Calls the functionality from the main file into the GUI

#This version aims to allows the user to input their 1-D differential equation and apply Euler's method to approximate the solution of the DE at a point of the user's choice
def print_statement():
    """Displays the equations inputted on the GUI app."""    
    print(f"Equation: {equation_1.get()} with x1 = {initial_1.get()}")
    print(f"Equation: {equation_2.get()} with x2 = {initial_2.get()}")
    print(f"Equation: {equation_3.get()} with x3 = {initial_3.get()}")


display_app = Tk()

#Sets the title of the GUI interface
display_app.title("Dynamical System Solver")

#Sets the defaults dimensions of the application
display_app.geometry('1280x720+50+50')

#Define the properties of the Canvas including colour, and the dimensions.
equation_1 = StringVar()
initial_1 = StringVar()

equation_2 = StringVar()
initial_2 = StringVar()

equation_3 = StringVar()
initial_3 = StringVar()




Font = ("Times New Roman", 20, "bold")

#The following code sets up a grid holding the structure the GUI
frame = Frame(display_app)
Label(frame,text = 'Please Enter dx1dt: ',font = Font).grid(row = 0, column=0,sticky = 'w')
eqn1 = Entry(frame,width = 25, textvariable=equation_1 )
eqn1.grid(row = 0, column= 1)
Label(frame,text = 'x1: ',font = Font).grid(row = 0, column=2,sticky = 'w')
inital_con1 = Entry(frame,width = 10,textvariable= initial_1)
inital_con1.grid(row = 0, column= 3)



Label(frame,text = 'Please Enter dx2dt: ',font = Font).grid(row = 1, column=0,sticky = 'w')
eqn2 = Entry(frame,width = 25,textvariable = equation_2)
eqn2.grid(row = 1, column= 1)
Label(frame,text = 'x2: ',font = Font).grid(row = 1, column=2,sticky = 'w')
inital_con2 = Entry(frame,width = 10,textvariable= initial_2)
inital_con2.grid(row = 1, column= 3)



Label(frame,text = 'Please Enter dx3dt: ',font = Font).grid(row = 2, column=0,sticky = 'w')
eqn3 = Entry(frame,width = 25,textvariable=equation_3)
eqn3.grid(row = 2, column= 1)
Label(frame,text = 'x3: ',font = Font).grid(row = 2, column=2,sticky = 'w')
inital_con3 = Entry(frame,width = 10,textvariable= initial_3)
inital_con3.grid(row = 2, column= 3)

Button(frame, text = 'Solve Dynamical System', command = print_statement).grid(row = 3, columnspan=4,sticky='ew')



frame.pack()
display_app.mainloop()
