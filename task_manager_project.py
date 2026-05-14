class Task:
    def __init__(self,title):
        self.title = title
        self.status = "todo"

    def complete(self):
        self.status= "done"

    def __str__(self):
        return (f"[{self.status.upper()}] {self.title}")

task = []
def  add_task(title): 
        t = Task(title)
        task.append(t)
        return(f"you added {title} sucessfully")



    

    


    
add_task("cooking")
add_task("going gym")
print(add_task("gg"))
for i in task:
     print(i)








    
   