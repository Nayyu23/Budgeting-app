class Budget:
    def __init__(self, start):
        self.budget = start
        self.moneyIn = []
        self.moneyOut = []
        self.inNotes = []
        self.outNotes = []

    
    def inNote(self, str1):
        self.inNotes.append(str1)

    def outNote(self, str1):
        self.outNotes.append(str1)

    def add(self, num):
        self.budget += num
        self.moneyIn.append(num)
        ques = str(input("Do you want to add a note? (y/n) "))

        if "y" in ques:
            tempn = input("Enter note here: ")
            self.inNote(tempn)

        else:
            self.inNote(" ")


    def subtract(self, num):
        self.budget -= num
        self.moneyOut.append(num)
        ques = str(input("Do you want to add a note? (y/n) "))

        if "y" in ques:
            tempn = input("Enter note here: ")
            self.outNote(tempn)

        else:
            self.outNote(" ")
    
    def totalMoneyIn(self):
        totalMoney = 0
        for i in range (len(self.moneyOut)-1):
            totalMoney += self.moneyIn[i]

        return totalMoney
    
    def totalMoneyOut(self):
        totalMoney = 0
        for i in range (len(self.moneyOut)-1):
            totalMoney += self.moneyOut[i]
            
        return totalMoney

    def __str__ (self):
        return("Total earnings: " + str(self.totalMoneyIn()) + "\n" + "Total spending: " + str(self.totalMoneyOut()) + "\n" + "Money left: " + str(self.budget) + "\n")

mainBudget = Budget(0)

while True:
    print("\n")
    print("\n")
    print("Hello! Welcome to the Main Menu.\nType the number of the option you need to use.")
    print("_______________________________________________\n")
    selection = input("1. Add to budget\n2. Subtract from budget\n3. Print current budget info\n4. Exit program\n\n")
    print("\n")

    if selection == "1":
        money = input("Enter amount to add: ")
        mainBudget.add(float(money))
    
    elif selection == "2":
        money = input("Enter amount to subtract: ")
        mainBudget.subtract(float(money))
    
    elif selection == "3":
        print(mainBudget)
    
    else:
        break

        
