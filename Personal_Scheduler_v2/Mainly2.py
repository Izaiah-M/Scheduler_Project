import datetime

from ConnectingDataBase2 import insert_task

# A function that will help us generate days in form of lists, because different days have different tasks
def monthGenerator(days):
    month = []
    for i in range(0,days+1):
        if i == 0:
            month.append(None)
        else:
            month.append([])
    
    return month

# Create a task and store it in a database
def CreateTask():
    title = str(input("Enter task title: \n"))
    cat = str(input("Enter task category  (Personal or School): \n"))
    desc = str(input("Enter task description: \n"))
    date = int(input("Enter date you want the task to be done (1 to 30): \n"))
    start = int(input("Enter time you want the task to start (0 to 12): \n"))
    end = int(input("Enter time you want the task to end (13 to 23): \n"))

    # For putting the task into the data base
    insert_task(title, cat, desc,start,end,date)

    print("You have added a task: " + desc + ", which is to be done on: " + str(date) + "\n")

    # A loop that will help a user create tasks just incase they want to creat more than once.
    another = input("Would you like to add another task? y/n: \n")
    if another == "y":
        CreateTask()
    elif another == "n": 
        print("Alright, Have a productive day!!")



