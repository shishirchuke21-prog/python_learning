# class Vehicle:
#     def __init__(self, brand, speed, fuel_type):
#         self.brand = brand
#         self.speed = speed
#         self.fuel_type = fuel_type

#     def move(self):
#         return f"{self.brand} is moving"

#     def __str__(self):
#         return f"{self.brand} | Speed: {self.speed} | Fuel: {self.fuel_type}"


# class Car(Vehicle):
#     def __init__(self, brand, speed, fuel_type, doors):
#         super().__init__(brand, speed, fuel_type)
#         self.doors = doors

#     def honk(self):
#         return f"{self.brand} goes beep beep"


# class Truck(Vehicle):
#     def __init__(self, brand, speed, fuel_type, capacity):
#         super().__init__(brand, speed, fuel_type)
# #         self.capacity = capacity

#     def load(self):
#         return f"{self.brand} is loading {self.capacity}kg"


# car = Car("Toyota", 120, "Petrol", 4)
# truck = Truck("Volvo", 80, "Diesel", 5000)

# print(car)
# print(car.move())
# print(car.honk())

# print(truck)
# print(truck.move())
# print(truck.load())


class Animal:
    def __init__(self,name,age):
        self.name= name
        self.age=age

    def eat(self):
        return(f"{self.name} is eating")
    def sleep(self):
        return(f"{self.name} is sleeping")
    
    def __str__(self):
        return(f"Animal {self.name}. | {self.age}")   #it runs automatically when you run an object
    
class Dog(Animal):
    def __init__(self, name, age,breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        return(f"{self.name} say woof woof")
    def fetch(self):
        return(f"{self.name} is fetching the ball") 
    
class Bird(Animal):
    def __init__(self, name, age,can_fly):
        super().__init__(name, age)
        self.can_fly=can_fly

    def chirp(self):
        return(f"{self.name} says tweeet tweet")
    
    def fly(self):
        if ( self.can_fly==True ):
            return (f"{self.name} can fly")
        else:
            return(f"{self.name} cannot fly")


dog = Dog("reo", 6 , "labrador")
dog2 = Dog("bruno", 1 , "outdoor")
bird1 = Bird("tweety", 1 , False)

print(dog.fetch())
print(dog.eat())
print(dog2)
print(bird1)

       
        
    
    