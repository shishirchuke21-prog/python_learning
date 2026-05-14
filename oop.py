class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
            return(f"HI I am {self.name} {self.age} years old from {self.city}")
        
    def is_adult(self):
            if (self.age>=18):
                return True
            else:
                  return False
                   
            

                
p1 = Person("Shishir", 22, "Mumbai")
p2 = Person("Tommy", 15, "London")

print(p1.introduce())
print(p1.is_adult())
print(p2.introduce())
print(p2.is_adult())

        