#PSEUDOCODE
#create Calculator Class
class Calculator:
    #create functions;
    #get number inputs and arithmetic operation from user
    def user_inputs(self):
        while True:
            try:
                #get number inputs
                self.first_num =float(input("Enter your FIRST NUMBER:  " ))
                self.second_num =float(input("Enter your SECOND NUMBER:  "))
                #get arithmetic operation
                self.operation = str(input("Choose an operation: \n If add, enter '+',\nIf subtract,enter '-'\n\tIf multiply,enter '*'\n\tIf divide,enter '/' "))
                break
            except:
                print("INVALID INPUT!!!\nPlease enter a valid values")
                continue
        #calculate the inputs
        #display the calculated results