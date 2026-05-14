scores = {
    "Arjun": 85,
    "Priya": 92,
    "Rahul": 78,
    "Sara": 95,
    "Kiran": 88
}

total_score = 0
for i in scores.values():
    total_score=total_score + i

print(f"Total score : {total_score}")
