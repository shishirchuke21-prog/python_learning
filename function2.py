# def is_even(n):
  
#     if(n%2==0):
#         return True
#     else:
#         return False

# print(is_even(8))

# def calculate_area(shape,width,height= 0):
#     if (shape == "rectangle"):
#         return(f"Area of Rectangle is {width*height}")
#     if (shape == "square"):
#         return(f"Area of square is {width*width}")
    
# print(calculate_area("rectangle",8,4))
# print(calculate_area("square",8))
    
def find_max(n):
    numbers=n[0]
    for i in n:
        if(numbers<i):
            numbers=i
    return numbers
print(find_max([4,5,8,9]))


def count_vowel(words):
    word=["a","e","i","o","u"]
    count=0
    for I in words:
     if I in word:
        count += 1
    return count
     
print(count_vowel("shishir"))
print(count_vowel("education"))


def reverse_word(word):
   splt=word.split()
   reversed_word = splt[::-1]
   final_word=" ".join(reversed_word)
   print(final_word)
reverse_word("hello shishir k cha khabar")
   
   


    