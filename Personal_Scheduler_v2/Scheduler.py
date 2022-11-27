from Mainly2 import CreateTask
from SortAlgos2 import tasks_of_specific_day, remove_task_from_specific2,busy_day,Upcomingtasks, all_tasks, listing_all_personal, listing_all_school


# Listing the tasks
def listTasks():
    print("1. All tasks in Month (Both Personal and School tasks shall be listed)")
    print("2. Personal tasks")
    print("3. School tasks")
    print("4. List tasks of a specific day")
    print("5. View upcoming Tasks")
    print("")
    choice = input()
    print("")

    if (choice == str(1)):
        all_tasks()
    elif (choice == str(2)):
        listing_all_personal()
    elif (choice ==  str(3)):
        listing_all_school()
    elif (choice == str(4)):
        day = int(input("Which day's tasks would you like to view: \n"))
        tasks_of_specific_day(day)
        busy_day(day)
    elif (choice == str(5)):
        Upcomingtasks()

def removingTask():
    day = int(input("Which day would you like to delete task from: \n"))
    tasks_of_specific_day(day)

    m = int(input("Enter the Id of the task: \n"))
    remove_task_from_specific2(day, m)


    

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