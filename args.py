# model.fit(X, y, epochs=10, batch_size=32)

# def multiply(*args):
#     final_number=1

#     for i in args:
#         final_number = i*final_number

#     return final_number
# print(multiply(2,3,5,6,7,8))

def build_profile(**kwargs):
    for key, value in kwargs.items():
     print(f"{key}:{value}")
             

build_profile(name="shishir", age=21)
    




    