from datetime import date
class Task():
    def __init__(self,title):
        self.title=title
        self.status="to_do"
        self.created_date = date.today()
    def complete(self):
        self.status="done"
    def __str__(self):
        return(f"{self.status.upper()} {self.title} created; {self.created_date}")

        
def add_task(tasks,title):
    T=Task(title)
    tasks.append(T)
    return tasks

t=Task("study python")
print(t)

my_task=[]
add_task(my_task,"pyp")
add_task(my_task,"pyp")
for mytsk in my_task:
  print(mytsk)
  

    

