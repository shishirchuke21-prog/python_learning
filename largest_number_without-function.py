numbers = [34, 12, 89, 5, 67, 23, 90, 45, 11, 78]
largest = numbers[0]
smallest = numbers[0] #pull out any 1st number from the list
for i in numbers:
    if(i>largest):
       largest=i# it is inside the for loop it is going to rint only 1 number 
    if(i<smallest):
           smallest=i

      

print(largest)
print(smallest)