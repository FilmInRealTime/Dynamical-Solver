import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from sympy import *

def DE_formation():
    """This function takes the users input and puts it into a form so we can change how many
    equations we consider."""
    num_equation = check_numeric("How many equations would you like to enter?: ",1)
    
    if num_equation > 3:
        print('Are you sure you would like to solve such a big system? The application is made for 3 or less systems.')

    while num_equation <= 0:
        num_equation = int(input("Oops, you can't have a negative number of equations, please enter a valid input:"))


    lower_bound, upper_bound = solving_bounded(num_equation)
    j = 0
    equations = []
    variables  = []
    equation_names = []
    print(f"You are solving a dynamical system with {num_equation} equations. Your variables have the form x = (t,x1,...xn), where n is the number of equations you wish to solve for.")
    #This while loop goes through and defines the number of variables required for the differential equations in the form x1,...,xn. The time
    #dependent variable 't' is automatically defined.

    while j < num_equation:
        j += 1
        temp_equation = read_string(f"Type you're derivative here. f{j}(x) =  ")
        equations.append(temp_equation)
        variables.append("x{0}".format(j))
        equation_names.append("dx{0}dt".format(j))
        
    print(f"Your differential equations are named {equation_names}")
    initial_vec = initial_values(j)
    return equations, initial_vec,lower_bound,upper_bound, variables, equation_names

def initial_values(j):
    """This function forms a vector with the initial conditions for our first order differential 
    equation."""
    initial_vector = []
    for i in range(j):
        initial_vector.append(check_numeric("Please enter your initial value here: ",0))
    return np.array(initial_vector)

def solving_bounded(j):
    """This function sets up the bounds in the dimension's we are solving on"""
    lower_bound = check_numeric("Please enter your lower bound for t here: ",0)
    upper_bound = check_numeric("Please enter your upper bound for t here: ",0)
    return lower_bound,upper_bound
    

def check_numeric(string, j):
    """This function checks if the input is numeric and if it is not then
    pass an error prompting to the user to put in a valid input."""
    
    #The is_numeric variable is a trigger variable. It is defaulty set to be False to ensure all checks are done
    is_numeric = False

    while is_numeric == False:
        #The following if statement checks if we are testing for a float or interger.
        if j == 0:
            try:
                user_value = float(eval(read_string(string)))
                is_numeric = True
            except ValueError:
                is_numeric = False
                print("Please enter an float")
        else:
            
            try:
                user_value = int(read_string(string))
                is_numeric = True
            except ValueError:
                is_numeric = False
                print("Please enter an integer")

    
    return user_value

def f(v,t,en,id,vars):
    """This function defines the vector and equations being used."""
    print(f"t: {t}, v: {v}, en: {en}, id: {id}, vars: {vars}")
    info = []
    for j in range(len(id)):
        locals()[vars[j]] = v[j]
    for j in range(len(id)):
        x = id[j]
        locals()[id[j]] = eval(en[j])
        info.append(locals()[id[j]])
    return np.array(info)



def read_string(string):
    """This function prompts the user to enter the desired information"""
    user_input = input(string)
    return user_input


def modified_eulers(x0,t,h,en,id,variables):
    y = [x0]
    """This function defines modified euler's method, a method we use to solve first order differential equations."""
    for i in range(int((1/h) -2)):
        y.append(y[i] + (h/2)*(f(y[i],t[i],id,en,variables) + f(t[i] + h , y[i] + h*f(t[i],y[i],id,en,variables),id,en,variables)))
    return y



def eulers_method(x0,t,h,en,id,variables):
    y = [x0]
    """This function defines Euler's method, another method we use to solve first order differential equations"""
    for i in range(int((1/h) -2)):
        y.append(y[i] + h*f(y[i], t[i],id,en,variables))
    return y



def plot_solution(t,x):
    """This function plots the information that the user would like to know"""
    plt.plot(t,x)
    plt.show()



def continuity_check():
    """This function evaluates all inputted functions and determines whether there are any discontinuities, 
    and stores them. These will be prompted to the user before they choose their domain of integration."""

    #We begin by 

def plot_func():
    """This function plots the solution either in a time series, or phase portraits."""
    

def main():
    """The main function wraps all the other define functions into a line of processes"""
    input_derivative, initia_vec, lower_bound, upper_bound, variables, equation_names = DE_formation()
    #Note to self, I think I could simplify this down onto one line and have a list containing the required strings.
    intervals = int(check_numeric("Please enter the number of steps you would like to take: ",1))
    method = read_string("Enter the method you would like to use. (Select from Euler's Method, Modified Euler's Method): ")
    #The linspace function from the numpy package defines the grid for which we will be plotting on.
    h = 1/(1+intervals)
    t = np.linspace(lower_bound,upper_bound,intervals)
    x = odeint(f,initia_vec,t, args=(input_derivative,equation_names,variables))
    plot_solution(t,x,variables,equation_names)

