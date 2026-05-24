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
def view_task():
     if(len(task)==0):
          return("there is no any task")
     else:
          for i , j in  enumerate(task):    #enumerate get the index number of the value
               print(f"{i+1} . {j}")
def complete_task(index):
    try:
        task[index - 1].complete()
        print(f"{task[index - 1]}task completed")
    except IndexError:
        print("invalid task number")
def delete_task(index):
     try:
          removed = task.pop(index - 1)
          print (f"deleted ; {removed.title}")

     except IndexError:
          print("invalid task number")
def menu():
     while True:
         print("\n===== Task Manager =====")
         print("1. Add task")
         print("2. View tasks")
         print("3. Complete task")
         print("4. Delete task")
         print("5. Quit")

         choose = int(input("enter a number"))

         if choose == 1:
              title = input("enter a task")
              print(add_task(title))

         elif choose==2:
              (view_task())
         elif choose==3 :
              (view_task())
              n=int(input("enter a number which task to complete"))
              complete_task(n)
         elif choose==4:
                (view_task())
                n=int(input("enter a number which task to delete"))
                delete_task(n)
         elif choose==5 :
              print("good bye")
              break
         else:
              print("invalid num")

          
          
menu()








    
   