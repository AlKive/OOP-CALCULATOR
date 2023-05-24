# BABIERA,ALEXA | CMPE-103-OBJECT-ORIENTED PROGRAMMING|BSCPE 1-5 | MAY 24,2023
# Assignment 7 : Redo the Calculatir program applying the OOP concepts.

from colorama import Back, Fore, Style, init
import time

from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
ws = Tk()

#create Calculator Class
class Calculator:
    #create functions;
    #get number inputs and arithmetic operation from user
    def user_inputs(self):
        while True:
            try:
                #get number inputs
                self.first_number = simpledialog.askfloat("firstNumber", "Enter your FIRST NUMBER:  ", parent = ws)
                self.second_number = simpledialog.askfloat("secondNumber", "Enter your SECOND NUMBER:  ", parent = ws)
                #get arithmetic operation
                self.operation = simpledialog.askstring("Operation", "Choose an operation: \nIf add, enter '+' : \nIf subtract,enter '-' : \nIf multiply,enter '*' : \nIf divide,enter '/' : ", parent=ws)   
                break
            except:
                messagebox.showerror("INVALID INPUT!!!\nPlease enter a valid values", parent= ws)
                continue
            
    #calculate the inputs
    def Calculate(self) -> None:
    # If one of the arguments is missing, throw an error
        if (self.first_number and self.second_number and self.operation) == False:
            raise NameError("You're missing an argument/s, check your inputs!")
        try:
            self.first_number = float(self.first_number)
            self.second_number = float(self.second_number)
            # choosing peferred operation
            match self.operation:
                    case '+':
                        self.result = self.first_number + self.second_number
                    case '-':
                        self.result = self.first_number - self.second_number
                    case '*':
                        self.result = self.first_number * self.second_number
                    case '/':
                        try:
                            self.result = self.first_number / self.second_number
                        except ZeroDivisionError:
                            raise ZeroDivisionError("[ERROR] Division by Zero is not allowed!")
                    case _:
                        raise ValueError("UNSUPPORTED OPERATION")
        except ValueError:
            messagebox.showerror("UNSUPPORTED CHARACTER/ELEMENT")   
        
    def show_result(self):
        self.result = float(self.result)
        time.sleep (2)
        print(Fore.LIGHTRED_EX + "CALCULATED RESULT: " + Fore.LIGHTWHITE_EX +str(self.result))