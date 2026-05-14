# try:
#     number = int(input("enter number: "))
# except ValueError:
#     print("not a number")
# finally:
#     print("program finished")    # runs always — error or not





# def divide(a, b):
#     try:
#         number = a / b
#         return number
#     except ZeroDivisionError:
#         return "cannot divide by zero"

# print(divide(10, 2))    # 5.0
# print(divide(10, 0))    # cannot divide by zero

# def get_element(my_list, index):
#     try:
#         return my_list[index]    # access element at index
#     except IndexError:
#         return "index out of range"

# print(get_element([1,2,3,4,5,6],9))

def covert_int(value):
    try:
        number=int(value)
        return number
    except ValueError:
        return "invalid input"
        
        
print(covert_int("hh"))