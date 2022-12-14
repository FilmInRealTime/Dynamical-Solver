from cgitb import text
from re import L
from tkinter import *
from tokenize import String
#We call the file GUI_main python script into our GUI interface so we can solve our ODEs.
import GUI_main as mn
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
#Calls the functionality from the main file into the GUI
plot_status = False

fig = None
plot1 = None
display_app = Tk()
plot_status = False
#This version aims to allows the user to input their 1-D differential equation and apply Euler's method to approximate the solution of the DE at a point of the user's choice
def print_statement():
    global canvas
    global plot_status
    # if plot_status == True:
    #     clear(canvas)
    """Displays the equations inputted on the GUI app."""   
    f_eqn1 = equation_1.get()
    f_eqn2 = equation_2.get()
    f_eqn3 = equation_3.get()
    #We combine the equations into a list that will later be sent to the main function for evaluation.
    equations = [f_eqn1, f_eqn2,f_eqn3]

    #We grab the inital conditions for the problems that we wish to solve.
    ic1 = initial_1.get()
    ic2 = initial_2.get()
    ic3 = initial_3.get()
    #We combine the initial conditions for the problems we wish solve, matching the position in the list to the cooresponding equation
    initial_conditions = [ic1,ic2,ic3]
    #Defines the bounds of our function
    lower_bound = float(lb.get())
    upper_bound = float(ub.get())
    bounds = [lower_bound,upper_bound]

    #Temporary test to ensure all fields are being grabbed
    print(f"Equation: {f_eqn1} with x1 = {ic1}")
    print(f"Equation: {f_eqn2} with x2 = {ic2}")
    print(f"Equation: {f_eqn3} with x3 = {ic3}")
    x,t = mn.main(equations,initial_conditions,bounds)
    
    #All the important information for the plot.
    fig = Figure(figsize=(8,4), dpi = 100)
    plot1 = fig.add_subplot(111)
    plot1.set_xlabel("t")
    plot1.set_ylabel("Solution")
    plot1.set_title("Approximate solution to the Dynamical System")
    plot1.plot(t,x[:,0], label ='Solution to x1')
    plot1.plot(t,x[:,1], label ='Solution to x2')
    plot1.plot(t,x[:,2], label ='Solution to x3')
    plot1.legend()

    canvas = FigureCanvasTkAgg(fig, master = display_app)
    canvas.draw()
    canvas.get_tk_widget().pack()
    plot_status = True


def clear(canvas):
    canvas.get_tk_widget().pack_forget()




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

lb = StringVar()
ub = StringVar()


Font = ("Times New Roman", 20, "bold")

#The following code sets up a grid holding the structure the GUI
text= 'This app assumes you are solving \n a dynamical system using three equations.'
frame = Frame(display_app)
#Creates the required input from the user for the first equation
Label(frame,text = f'{text}',font = Font).grid(row = 0, columnspan=3,sticky = 'w')

Label(frame,text = 'Please Enter dx1dt: ',font = Font).grid(row = 1, column=0,sticky = 'w')
eqn1 = Entry(frame,width = 25, textvariable=equation_1 )
eqn1.grid(row = 1, column= 1)
Label(frame,text = 'x1: ',font = Font).grid(row = 1, column=2,sticky = 'w')
inital_con1 = Entry(frame,width = 10,textvariable= initial_1)
inital_con1.grid(row = 1, column= 3)


#Creates the required input from the user for the second equation
Label(frame,text = 'Please Enter dx2dt: ',font = Font).grid(row = 2, column=0,sticky = 'w')
eqn2 = Entry(frame,width = 25,textvariable = equation_2)
eqn2.grid(row = 2, column= 1)
Label(frame,text = 'x2: ',font = Font).grid(row = 2, column=2,sticky = 'w')
inital_con2 = Entry(frame,width = 10,textvariable= initial_2)
inital_con2.grid(row = 2, column= 3)


#Creates the required input from the user for the third equation
Label(frame,text = 'Please Enter dx3dt: ',font = Font).grid(row = 3, column=0,sticky = 'w')
eqn3 = Entry(frame,width = 25,textvariable=equation_3)
eqn3.grid(row = 3, column= 1)
Label(frame,text = 'x3: ',font = Font).grid(row = 3, column=2,sticky = 'w')
inital_con3 = Entry(frame,width = 10,textvariable= initial_3)
inital_con3.grid(row = 3, column= 3)

Label(frame,text = 'Bounds: ',font = Font).grid(row = 4, column=0,sticky = 'w')
lower_bound = Entry(frame,width = 10,textvariable=lb)
lower_bound.grid(row = 4,column = 1,sticky = 'w')

upper_bound = Entry(frame,width = 10,textvariable=ub)
upper_bound.grid(row = 4,column = 2,sticky = 'w')

Button(frame, text = 'Solve Dynamical System', command = print_statement).grid(row = 5, columnspan=4,sticky='ew')




frame.pack()
display_app.mainloop()
