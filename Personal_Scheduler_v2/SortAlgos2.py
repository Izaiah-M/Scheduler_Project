import datetime
from ConnectingDataBase2 import list_all_tasks, remove_tasks 
from Mainly2 import monthGenerator
from Basic_Binary_search import binary_search


# A list that holds all the tasks pulled from the database.
tasks = list_all_tasks()

# A list that contains the days in the month of November, these days are in form if lists
November = monthGenerator(30)

def all_tasks():
    for task in tasks: #this runs in O(n)
        print(task)

# Sorting personal tasks
def personal_tasks():
    personal = []
    for task in tasks:
        if task.category == "Personal": #O(n)
            # print(task)
            personal.append(task)
    return personal

def listing_all_personal():
    personal = personal_tasks()
    for task in personal:       #O(n)
        print(task)

# Sorting school tasks
def school_tasks():
    school = []
    for task in tasks:
        if task.category == "School":   #O(n)
            # print(task)
            school.append(task)
    return school

def listing_all_school():
    school = school_tasks()
    for task in school:     #O(n)
        print(task)

# sorting different tasks to their respective days.
def day_tasks():
    for task in tasks:                  #O(n)
        November[task.dueDate].append(task)
    return November

task_specific = day_tasks()

# Function to return tasks of a specific day.
def tasks_of_specific_day(date):            #O(n^2)
    for day in range(len(task_specific)):
        if day == date:
            for task in task_specific[day]:
                print(task)

# A function to remove particular task from a given day with the use of our searchTasks function
def remove_task_from_specific2(date,num):
    lists = SearchTasks(date)                   #O(log(n))
    for task in lists:
        if task.TaskNo == num:
            task.iscompleted = True
            print("Task #" + task.description + " has been completed")
            task_specific[date].remove(task)
            remove_tasks(num)

# Function to check the busy days in the month basing off how many tasks are in the day/list
def busy_days_in_month():
    for day in task_specific:       #O(n)
        if type(day) == list and len(day) >= 3:
            print("{} is a busy day".format(task_specific.index(day)))       

# Function to check how busy an individual day is
def busy_day(day):
    if type(task_specific[day]) == list and len(task_specific[day]) >= 3:   #O(1)
        print("{} is a busy day".format(day))
    else:
        print(f"{day} is not busy")

# Function to search for tasks using a moded binary search
def SearchTasks(item):
    task_specific = day_tasks()
    ind = binary_search(task_specific,item)
    return task_specific[int(ind)]

    

# A Function to help notify the user of upcoming tasks/tasks fast approaching
def Upcomingtasks():
    x = datetime.datetime.now()
    dateToday = int(x.strftime("%d"))

    for i in range(dateToday,len(task_specific)):   #O(n)
        if type(task_specific[i]) == list:
            for task in task_specific[i]: 
             print(task)




def returntasks():
    tasks = list_all_tasks()
    return tasks

