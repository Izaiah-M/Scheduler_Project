from Mainly2 import CreateTask
from SortAlgos2 import personal_tasks, school_tasks
from SortAlgos2 import all_tasks


# Listing the tasks
def listTasks():
    print("1. All tasks (Both Personal and School tasks shall be listed)")
    print("2. Personal tasks")
    print("3. School tasks")
    print("")
    choice = input()
    print("")

    if (choice == str(1)):
        all_tasks()
    elif (choice == str(2)):
        personal_tasks()
    elif (choice ==  str(3)):
        school_tasks()

def removingTask():
    print("What category does the task fall under")
    print("1. Personal")
    print("2. School")
    print("")
    choose = input()
    print("")

    if choose == str(1):
        personal_tasks()
        print("")
        print("Enter the id of the task you would like to remove: ")
        num = input()
        print("")
        remove_personal_task(num)
        print("")
        list_personal_tasks()
        print("")
    elif choose == str(2):
        list_school_tasks()
        print("")
        print("Enter the id of the task you would like to remove: ")
        add = input()
        print("")
        remove_school_task(add)
        print("")
        list_school_tasks()
        print("")


    

# Here we are calling it like our main function, its what is prompted to create a schedule.
def creating_A_schedule():
    print("**************************************")
    print("Heloo, welcome to your scheduler!!!")
    print("")
    print("What would you like to do?")
    print("")
    print("1. Create a new task")
    print("2. View pending tasks")
    print("3. Mark task as completed")
    print("")
    option = input()
    print("")

    if (option == str(1)):
        CreateTask()
    elif(option == str(2)):
        listTasks()
    elif(option == str(3)):
        removingTask()
    print("")
    print("Go back to Main menu? y/n")
    choice = input()
    print("")
    if choice == "y":
        creating_A_schedule()
    elif choice == "n":
        print("Happy productivity!!")
    

creating_A_schedule()