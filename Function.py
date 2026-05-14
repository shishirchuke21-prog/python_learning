# def greet(name):
#     return(f"hello {name} welcome to python")

# print(greet("shishir"))
# greet("ankit")
# greet("ronik")

def bmi(weight,height):
    result= weight/(height*height)
    return round(result,2)
print(bmi(68,1.75))
print(bmi(88,1.99))
    
def palindrome(word):
    new_word= word[::-1]
    if(word==new_word):
        return True
    else:
        return False
# check_palindrome= palindrome(word)
print(palindrome("car"))
palindrome("racecar")


def create_profile(name,age, role = "student"):
 return(f"Name ; {name} Age : {age} Role ; {role} ")
    
print(create_profile("shishir",21,"engibneer"))

        
    

