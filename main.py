class Budget:
    def __init__(self, start): # Initializing the class
        self.budget = start
        self.moneyIn = []      # Used to record all the times money is added
        self.moneyOut = []     # Used to record all the times money is subtracted
        self.inNotes = []      # Used to record each time a note is added (when money is added)
        self.outNotes = []     # Used to record each time a note is added (when money is subtracted)

    # Add a note when money is added to the budget
    def inNote(self, str1):
        self.inNotes.append(str1)

    # Add a note when money is removed from the budget
    def outNote(self, str1):
        self.outNotes.append(str1)

    '''
    Adds specified amount to the current budget
    Option to add a note along with the change in funds
    '''
    def add(self, num):
        self.budget += num
        self.moneyIn.append(num)
        ques = str(input("Do you want to add a note? (y/n) "))

        if "y" in ques:
            tempn = input("Enter note here: ")
            self.inNote(tempn)

        else:
            self.inNote(" ")


    '''
    Subtracts specified amount from the current budget
    Option to add a note along with the change in funds
    '''
    def subtract(self, num):
        self.budget -= num
        self.moneyOut.append(num)
        ques = str(input("Do you want to add a note? (y/n) "))

        if "y" in ques:
            tempn = input("Enter note here: ")
            self.outNote(tempn)

        else:
            self.outNote(" ")
    

    '''
    Loops through the list of money added and sums it up to determine total inflow of money
    '''
    def totalMoneyIn(self):
        totalMoney = 0
        for i in self.moneyIn:
            totalMoney += i

        return totalMoney
    

    '''
    Loops through the list of money subtracted and sums it up to determine total outflow of money
    '''
    def totalMoneyOut(self):
        totalMoney = 0
        for i in self.moneyOut:
            totalMoney += i
            
        return totalMoney


    '''
    Custom print statement for the class
    Prints:

    Total earnings: sum of all money added
    Total spending: sum of all money subtracted
    Money left: money left in the budget (total earnings - total spendings)
    '''
    def __str__ (self):
        return("Total earnings: " + str(self.totalMoneyIn()) + "\n" + "Total spending: " + str(self.totalMoneyOut()) + "\n" + "Money left: " + str(self.budget) + "\n")

mainBudget = Budget(0) # Initializes an object for the budget (starting at 0)


'''
Infinite loop that keeps prompting the user to make a selection from the main menu to access features of the app.
Option 1 lets them add money to the budget
Option 2 lets them subtract money from the budget
Option 3 lets them print a budget summary (Total money in, total money out, and money left over)
Option 4 breaks the loop and exits the app
'''
while True:
    print("\n")
    print("\n")
    print("Hello! Welcome to the Main Menu.\nType the number of the option you need to use.")
    print("_______________________________________________\n")
    selection = int(input("1. Add to budget\n2. Subtract from budget\n3. Print current budget info\n4. Exit program\n\n"))
    print("\n")

    if selection == 1:
        money = input("Enter amount to add: ")
        mainBudget.add(float(money))
    
    elif selection == 2:
        money = input("Enter amount to subtract: ")
        mainBudget.subtract(float(money))
    
    elif selection == 3:
        print(mainBudget)
    
    elif selection == 4:
        break
    
    else:
        print("Invalid selection")

        
