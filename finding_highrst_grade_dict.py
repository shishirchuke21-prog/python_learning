grades = {
    "Arjun": 85,
    "Priya": 92,
    "Rahul": 78,
    "Sara": 95,
    "Kiran": 88
}
top_student = "none"
top_grade = 0
for key , value in grades.items():
    if(top_grade<value):
        top_student= key
        top_grade = value
print(top_student)
print(top_grade)

  
  