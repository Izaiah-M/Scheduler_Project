import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from SortAlgos2 import returntasks 

#git
TaskCompiler = returntasks()
#function that turns the task list into  dictionaries to be used as a dataframe
def TaskDict(list):
    tasklist = []
    for obj in list:
        tasklist.append(obj.__dict__)
    return tasklist

TaskDictList = (TaskDict(TaskCompiler))
dl_df = pd.DataFrame(TaskDictList)

dl_df['width'] = (dl_df.timeend) - (dl_df.timestart)

def DateChart(date):
    date_df = dl_df.loc[dl_df["dueDate"] == date]
    plt.barh(y=date_df['task'], width=date_df['width'], left=date_df['timestart'])
    plt.title("Gannt Chart Showing Tasks In Accordance With Their Deadlines")
    plt.xlabel("Duration For Tasks")
    plt.ylabel("Tasks At Hand")
    plt.savefig('Gannt Chart For Tasks.png')

