#An array to store the expense
expenses = []

#creating a function to add expense to array
def addExpense(amount, category):
    expense = {'amount':amount, 'category':category}
    expenses.append(expense)
    
    
#creating a function printMenu(opertions)
def printMenu():
    print("Please choose one of the operations: ")
    print("1.Add a new expense: ")
    print("2.Remove  an existing expense:")
    print("3.Display all expenses: ")
    print("\n")

#function displays the list
def listExpenses():
    print("\n Here is a list of your expenses.")
    print("-----------------------------------")
    counter= 0
    for expense in expenses:
        print("#", counter," - ",expense['amount']," - ",expense['category'])
        counter +=1
    print("\n\n")
    
#Function to remove an item from the list
def removeExpense():
    while True:
        listExpenses()
        print( "Enter the number of the expense you want to delete: ")
        try:
            expenseToRemove=int(input("- "))
            del expenses[expenseToRemove]
            break
        except:
            print("invalid please enter a valid number!")
            
#Main Function
if __name__ == "__main__":
    while True:
        ###Prompt the user
        printMenu()
        optionSelect = input("- ")
        
        #add expense option logic
        if(optionSelect =="1"):
            print("\n")
            print("how much was this expense? ")
            while True:
                try: 
                    amountToAdd = input("- ")
                    break
                except:
                    print("invalid input. please try again.")
            print("\n")
            print("What Category was this expense? ")
            while True:
                try:
                    category = input("- ")
                    break
                except:
                    print("invalid input. Please try again.")
            addExpense(amountToAdd, category)
            
        elif(optionSelect == "2"):
            removeExpense()
        elif(optionSelect == "3"):
            listExpenses()
        else:
            print("Invalid input please choose an option from the menu.")