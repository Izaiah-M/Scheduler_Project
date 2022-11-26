import random

from ConnectingDataBase2 import insert_task


# Here we are generating random data to play with in our data base.
titles = ["Title1","Title2","Title3","Title4","Title5","Title6","Title7","Title8"]
categories =["School","Personal"]
descriptions = ["This a sample description of a task","This also a sample description of a task","This another sample description of a task"]

def RandomizedValues():
    for i in range(0,45):
        title = random.choice(titles)
        cat = random.choice(categories)
        desc = random.choice(descriptions)
        start = random.randint(0,23)
        end = random.randint(0,23)
        date = random.randint(1,30)

        insert_task(title,cat,desc,start,end,date)


RandomizedValues()

