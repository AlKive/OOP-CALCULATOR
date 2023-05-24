# BABIERA,ALEXA | CMPE-103-OBJECT-ORIENTED PROGRAMMING|BSCPE 1-5 | MAY 24,2023
# Assignment 7 : Redo the Calculatir program applying the OOP concepts.

from colorama import Back, Fore, Style, init
import time

from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

ws = Tk()
ws.geometry("700x350")


#create Calculator Class
class Calculator:
    #create functions;
    #get number inputs and arithmetic operation from user
    def user_inputs(self):
        while True:
            try:
                #get number inputs
                self.first_number = simpledialog.askfloat("FIRST NUMBER", "Enter your FIRST NUMBER:  ", parent = ws)
                self.second_number = simpledialog.askfloat("SECOND NUMBER", "Enter your SECOND NUMBER:  ", parent = ws)
                if self.second_number == 0 :
                    raise ZeroDivisionError(messagebox.showerror("ZERO DIVISION ERROR","[ERROR] Division by Zero is not allowed!"))
                #get arithmetic operation
                self.operation = simpledialog.askstring("Operation", "Choose an operation: \nIf add, enter '+' : \nIf subtract,enter '-' : \nIf multiply,enter '*' : \nIf divide,enter '/' : ", parent=ws)   
                break
            except:
                messagebox.showerror("INVALID", "INVALID INPUT!!!\nPlease enter a valid values", parent= ws)
                continue
            
    #calculate the inputs
    def Calculate(self) -> None:
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
                            self.result = self.first_number / self.second_number
                        case _:
                            raise ValueError("UNSUPPORTED OPERATION")
            except ValueError:
                messagebox.showerror("VALUE ERROR", "UNSUPPORTED CHARACTER/ELEMENT")   
        
    def show_result(self):
        self.result = float(self.result)
        time.sleep (2)
        messagebox.showinfo("RESULT", "CALCULATED RESULT: " + str(self.result))