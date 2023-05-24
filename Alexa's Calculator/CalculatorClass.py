# BABIERA,ALEXA | CMPE-103-OBJECT-ORIENTED PROGRAMMING|BSCPE 1-5 | MAY 24,2023
# Assignment 7 : Redo the Calculatir program applying the OOP concepts.

from colorama import Back, Fore, Style, init
import time
#create Calculator Class
class Calculator:
    #create functions;
    #get number inputs and arithmetic operation from user
    def user_inputs(self):
        while True:
            try:
                #get number inputs
                self.first_number =float(input(Fore.YELLOW + "Enter your FIRST NUMBER:  " + Fore.LIGHTGREEN_EX))
                self.second_number =float(input(Fore.YELLOW + "Enter your SECOND NUMBER:  " + Fore.LIGHTGREEN_EX))
                #get arithmetic operation
                self.operation = str(input(Fore.GREEN +"Choose an operation: \nIf add, enter '+' : \nIf subtract,enter '-' : \nIf multiply,enter '*' : \nIf divide,enter '/' : " + Fore.YELLOW))   
                break
            except:
                print("INVALID INPUT!!!\nPlease enter a valid values")
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
            raise ValueError("UNSUPPORTED CHARACTER/ELEMENT")   
        
    def show_result(self):
        self.result = float(self.result)
        print(Fore.LIGHTRED_EX + "CALCULATED RESULT: " + Fore.LIGHTWHITE_EX +str(self.result))