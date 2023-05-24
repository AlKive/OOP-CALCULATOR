'''This program will call and run the functions from the Calculator Class file.'''
#import the class and object
from CalculatorClass import Calculator
#call Calculator
calcu = Calculator()
#Call and Loop the functions of the object
while True:
    #get input function
    calcu.user_inputs()
    #calculate function
    calcu.Calculate()
    #show result function
    calcu.show_result() 