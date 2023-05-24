#PSEUDOCODE
#create Calculator Class
class Calculator:
    #create functions;
    #get number inputs and arithmetic operation from user
    def user_inputs(self):
        while True:
            try:
                #get number inputs
                self.first_number =float(input("Enter your FIRST NUMBER:  " ))
                self.second_number =float(input("Enter your SECOND NUMBER:  "))
                #get arithmetic operation
                self.operation = str(input("Choose an operation: \n If add, enter '+',\nIf subtract,enter '-'\n\tIf multiply,enter '*'\n\tIf divide,enter '/' "))
                break
            except:
                print("INVALID INPUT!!!\nPlease enter a valid values")
                continue
            
    #calculate the inputs
    def Calculate(self) -> None:
    # If one of the arguments is missing, throw an error
        if (self.first_number and self.second_number and self.operation) == False:
            raise NameError("You're missing an argument/s, check your inputs!")
        if (self.first_number and self.second_number and self.operation) == True:
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
                raise ValueError("NUMBERS ONLY")   
    #display the calculated results
    def show_result(self):
        self.result = float(self.result)
        print("RESULT CALCULATED: " + str(self.result))