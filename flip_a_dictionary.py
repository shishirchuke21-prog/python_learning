original = {
    "a": 1,
    "b": 2,
    "c": 3
}

flipped_variable = {}
for key, value in original.items():
    flipped_variable[value] = key
print(flipped_variable)