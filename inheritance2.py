class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        return(f" Hi I am {self.name}, {self.age} years old")
    
class Student(Person):
    def __init__(self, name, age,student_id,grade):
        super().__init__(name, age)
        self.student_id=student_id
        self.grade=grade

    def study(self):
        return (f"{self.name} is studying")
    def __str__(self):
      return (f" Student ; {self.name} | Grade ; {self.grade}")
    
class Teacher(Person):
    def __init__(self, name, age,subject,salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def teach(self):
        return(f"{self.name} ios teaching python ")
    def __str__(self):
        return (f" Teacher : {self.name} | Subject ; {self.subject}")
    
    
s1 = Student("shishir", 22 , 231624 , "A")
t1= Teacher("MUSKAN" , 39 , "AI" , 100089)
print(s1)
print(s1.introduce())
print(s1.study())

print(t1)
print(t1.introduce())
print(t1.teach())
