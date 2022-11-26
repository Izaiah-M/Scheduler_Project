# Our class that will help us instantiate task objects

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
