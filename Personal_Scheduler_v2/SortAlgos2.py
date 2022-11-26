import datetime
from ConnectingDataBase2 import list_all_tasks, remove_tasks 
from Mainly2 import monthGenerator
from Basic_Binary_search import binary_search


# A list that holds all the tasks pulled from the database.
tasks = list_all_tasks()

# A list that contains the days in the month of November, these days are in form if lists
November = monthGenerator(30)

# def all_tasks():
#     tasks = list_all_tasks()
#     return tasks

# Sorting personal tasks
def personal_tasks():
    personal = []
    for task in tasks:
        if task.category == "Personal":
            # print(task)
            personal.append(task)
    return personal

# Sorting school tasks
def school_tasks():
    school = []
    for task in tasks:
        if task.category == "School":
            # print(task)
            school.append(task)
    return school



# sorting different tasks to their respective days.
def day_tasks():
    for task in tasks:
        November[task.dueDate].append(task)
    return November


# Function to return tasks of a specific day.
def tasks_of_specific_day(date):
    for day in range(len(task_specific)):
        if day == date:
            for task in task_specific[day]:
                print(task)

task_specific = day_tasks()

def remove_task_from_specific2(date,num):
    lists = SearchTasks(date)
    for task in lists:
        if task.TaskNo == num:
            task.iscompleted = True
            print("Task #" + task.description + " has been completed")
            task_specific[date].remove(task)
            remove_tasks(num)



# date = 10
# t = "11 This a sample description of a task, due: 10th"
# # task_specific[date].remove(task)
# print(task_specific[date])

def busy_days_in_month():
    for day in task_specific:
        if type(day) == list and len(day) >= 3:
            print("{} is a busy day".format(task_specific.index(day)))       

def busy_day(day):
    if type(task_specific[day]) == list and len(task_specific[day]) >= 3:
        print("{} is a busy day".format(day))
    else:
        print(f"{day} is not busy")


def SearchTasks(item):
    task_specific = day_tasks()
    ind = binary_search(task_specific,item)
    return task_specific[int(ind)]

def Upcomingtasks():
    days = day_tasks()
    x = datetime.datetime.now()
    dateToday = int(x.strftime("%d"))

    for i in range(dateToday,len(days)):
        if type(days[i]) == list:
            # for task in days[i]: 
            print(days[i])


# Upcomingtasks()
# remove_task_from_specific2()


print(task_specific)


