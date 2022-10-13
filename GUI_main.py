from unicodedata import numeric
import numpy as np
import scipy as sp
import matplotlib as plt
import matplotlib.pyplot as plt
from sympy import var
from sympy import sympify
from scipy.integrate import odeint

def DE_formation():
    """This function takes the users input and puts it into a form so we can change how many
    equations we consider."""
    num_equation = check_numeric("How many equations would you like to enter?: ",1)
    j = 0
    equations = []
    variables  = []
    equation_names = []

    while j < num_equation:
        j += 1
        temp_equation = read_string("Type you're derivative here: ")
        equations.append(temp_equation)
        variables.append("x{0}".format(j))
        equation_names.append("dx{0}dt".format(j))
        
    print(equation_names)
    initial_vec = initial_values(j)
    lower_bound, upper_bound = solving_bounded(j)
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
    lower_bound = check_numeric("Please enter your lower bound here: ",0)
    upper_bound = check_numeric("Please enter your upper bound here: ",0)
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

def f(t,v,en,id,vars):
    """This function defines the vector and equations being used."""
    info = []
    for j in range(len(id)):
        locals()[vars[j]] = v[j]
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
        y.append(y[i] + (h/2)*(f(t[i], y[i],id,en,variables) + f(t[i] + h , y[i] + h*f(t[i],y[i],id,en,variables),id,en,variables)))
    return y




def eulers_method(x0,t,h,en,id,variables):
    y = [x0]
    """This function defines Euler's method, another method we use to solve first order differential equations"""
    for i in range(int((1/h) -2)):
        y.append(y[i] + h*f(t[i], y[i],id,en,variables))
    return y



def plot_solution(t,x,j):
    """This function plots the information that the user would like to know"""
    dimension = int(check_numeric("How many dimensions would you like to plot,2 or 3: ",1))




def continuity_check():
    """This function evaluates all inputted functions and determines whether there are any discontinuities, 
    and stores them. These will be prompted to the user before they choose their domain of integration."""




def main():
    """The main function wraps all the other define functions into a line of processes"""
    input_derivative, initia_vec, lower_bound, upper_bound, variables, equation_names = DE_formation()
    #Note to self, I think I could simplify this down onto one line and have a list containing the required strings.
    intervals = int(check_numeric("Please enter the number of steps you would like to take: ",1))
    method = read_string("Enter the method you would like to use. (Select from Euler's Method, Modified Euler's Method): ")
    #The linspace function from the numpy package defines the grid for which we will be plotting on.
    h = 1/(1+intervals)
    t = np.linspace(lower_bound,upper_bound,intervals)

    vec = eulers_method(initia_vec,t,h,equation_names,input_derivative,variables)
    vec = np.array(vec)
    x1 = vec[:,0]
    plt.plot(t,x1)
    plt.show()


