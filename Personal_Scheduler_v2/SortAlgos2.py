from ConnectingDataBase2 import list_all_tasks
from Mainly2 import monthGenerator

# A list that holds all the tasks pulled from the database.
tasks = list_all_tasks()

# A list that contains the days in the month of November, these days are in form if lists
November = monthGenerator(30)

def all_tasks():
    tasks = list_all_tasks()
    for task in tasks:
        print(task)

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

# Sorting tasks that are due
def tasks_due():
    due = []
    for task in tasks:
        if task.iscompleted == False:
            # print(task)
            due.append(task)
    return due

# Sorting out completed tasks
# remove task from the list
# Modify to also remove from the database
def task_completed(taskNo):
    for task in tasks:
        if task.taskNo == taskNo:
            task.iscompleted = True
            print("Task #" + task.description + " has been completed")
            tasks.remove(task)

# sorting different tasks to their respective days.
def day_tasks():
    for task in tasks:
        November[task.dueDate].append(task)
    return November


# Function to return tasks of a specific day.
def tasks_of_specific_day(date):
    Nov = day_tasks()
    for day in range(len(Nov)):
        if day == date:
            for task in Nov[day]:
                print(task)

# tasks_of_specific_day(30)

