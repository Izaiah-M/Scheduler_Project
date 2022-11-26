import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from SortAlgos2 import returntasks 

#
TaskCompiler = returntasks()

def TaskDict(list):
    tasklist = []
    for obj in list:
        tasklist.append(obj.__dict__)
    return tasklist

TaskDictList = (TaskDict(TaskCompiler))
dl_df = pd.DataFrame(TaskDictList)
# print(dl_df)


dl_df['width'] = (dl_df.timeend) - (dl_df.timestart)
# print(dl_df)

plt.barh(y=dl_df['task'], width=dl_df['width'], left=dl_df['timestart'])
plt.title("Gannt Chart Showing Tasks In Accordance With Their Deadlines")
plt.xlabel("Duration For Tasks")
plt.ylabel("Tasks At Hand")

plt.savefig('Gannt Chart For Tasks.png')
