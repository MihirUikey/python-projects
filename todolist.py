#an array to store tasks
tasks = []

#creating a function to add tasks.
def addTask():
    task=input("Please Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")
    
#creating a function to display all tasks.
def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}: {task}")

#creating a function to delete a task.
def deleteTask():
    listTasks()
    try: 
        taskToDelete =int(input("Choose the # of the task you want to delete: "))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"The task '{taskToDelete}' has been deleted from the list.")
        else:
            print(f"Task #{taskToDelete} was not found.")  
    except:
        print("Invalid input.")
    
#main function that controls the program flow.
if __name__ == "__main__":
    #create a loop to run the app
    print("welcome to the to do list app: ")
    while True:
        print("\n")
        print("-------------------------------------")
        print("Please Select One of the Operations: ")
        print("1.Add a new task. ")
        print("2.Delete a task. ")
        print("3.List tasks")
        print("4.Quit ")
        
        #get user choice
        choice= input("Enter your choice: ")
        
        if(choice =="1"):
            addTask()
        elif(choice=="2"):
            deleteTask()
        elif(choice=="3"):
            listTasks()
        elif(choice=="4"):
            break
        else:
            print("Invalid Input. Please try again.")
print("-------------------------------")