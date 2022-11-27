import sqlite3
from Mainly2 import Task

conn = sqlite3.connect("Calendar.db")
c = conn.cursor()

# Method for inserting tasks into table
def insert_task(title, cat, desc,start,end,date):

    # The insert querry
    insert_query =   """INSERT INTO Task
                            (Task,Category,Description,Start,End,Deadline,IsComplete) 
                            VALUES 
                            (?,?,?,?,?,?,'False');"""

    # The data tupple takes in the values to be inserted into the db
    data_tuple = (title, cat, desc,start,end,date)
    c.execute(insert_query, data_tuple)
    conn.commit()  

def list_all_tasks():
    tasks = []
    c.execute("SELECT * FROM Task")
    rows = c.fetchall()

    # Making instances of the things inserted in the database
    for row in rows:
        Id = row[0]
        title = row[1]
        cat = row[2]
        desc = row[3]
        start = row[4]
        end = row[5]
        date = row[6]
        complete = row[7]

        task = Task(Id, title, cat, desc, date,start,end, complete)
        tasks.append(task)
    return tasks

def list_personal_tasks():
    c.execute("SELECT * FROM Task WHERE Category == 'Personal'")
    rows = c.fetchall()
    for row in rows:
        for task in row:
            print(task)

def list_school_tasks():
    c.execute("SELECT * FROM Task WHERE Category == 'School'")
    rows = c.fetchall()
    for row in rows:
        for task in row:
            print(task)

def remove_personal_task(taskId):
    e = 'DELETE FROM Task WHERE Id = ? AND Category == "Personal"'
    c.execute(e, (taskId,))
    conn.commit()
    # print("Task #" + str(taskId) + " complete")


def remove_school_task(taskId):
    e = 'DELETE FROM Task WHERE Id = ? AND Category == "School"'
    c.execute(e, (taskId,))
    conn.commit()
    print("Task #" + str(taskId) + " complete")

# print(list_all_tasks())