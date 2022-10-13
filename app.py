from tkinter import *
#We call the file GUI_main python script into our GUI interface so we can solve our ODEs.
import GUI_main as mn
#Calls the functionality from the main file into the GUI

#This version aims to allows the user to input their 1-D differential equation and apply Euler's method to approximate the solution of the DE at a point of the user's choice
display_app = Tk()
#Sets the title of the GUI interface
display_app.title("Dynamical System Solver")
#Sets the defaults dimensions of the application
display_app.geometry('1280x720+50+50')
#Makes the application not resizable
display_app.resizable(False,False)

#The next few lines will be the strings that prompt the user for their equations, initial conditions, etc.
equation_string = Label(text = "test")

canvas1 = Canvas(
    display_app,
    height = 1280,
    width = 500,
    bg ="grey",
    highlightthickness=0
)

equation = Entry(display_app)
canvas1.pack(side = 'left')
placeholder_text = "Enter Equation"
equation.insert(0,placeholder_text)
canvas1.create_window(70,60,window = equation)


display_app.mainloop()

mn.main()
