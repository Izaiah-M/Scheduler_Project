import datetime

# from ConnectingDataBase2 import insert_task

class Task:
    def __init__(self,TaskNo,task,category,description,dueDate: int,timestart, timeend,iscompleted):
        self.TaskNo = TaskNo
        self.task = task
        self.category = category
        self.description = description
        self.dueDate = dueDate
        self.timestart = timestart
        self.timeend = timeend
        self.iscompleted = iscompleted

    def __repr__(self):
        return str(self.TaskNo) + " " + self.description + ", due: " + str(self.dueDate) + "th"
    #     return f"\n------------------------------------------------------\nTitle: {self.task}\nCategory: {self.category}\nDue Date of Task: {self.dueDate}\nDescription: {self.description}\nCompleted: {self.iscompleted}\n------------------------------------------------------\n"


    def taskComplete(self):
        self.iscompleted = True

# Generating lists of the days in a month, that will hold the various tasks
def monthGenerator(days):
    month = []
    for i in range(0,days+1):
        if i == 0:
            month.append(None)
        else:
            month.append([])
    
    return month

November = monthGenerator(30)
# print(November)

def CreateTask():
    title = str(input("Enter task title: \n"))
    cat = str(input("Enter task category  (Personal or School): \n"))
    desc = str(input("Enter task description: \n"))
    date = int(input("Enter date you want the task to be done (1 to 30): \n"))
    start = int(input("Enter time you want the task to start (0 to 23): \n"))
    end = int(input("Enter time you want the task to end (0 to 23): \n"))

    # Creating task
    # task = Task(None, title, cat, desc,start,end,date)

    # For inserting our task into the appropriate day(index) in November
    # November[date].append(task)

    # For putting the task into the data base
    # insert_task(title, cat, desc,start,end,date)

    print("You have added a task: " + desc + ", which is to be done on: " + str(date) + "\n")

    another = input("Would you like to add another task? y/n: \n")
    if another == "y":
        CreateTask()
    elif another == "n": 
        print("Alright, Have a productive day!!")

    print(November)



# CreateTask() 
# print(November)
