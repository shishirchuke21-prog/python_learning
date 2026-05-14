cities = ("Mumbai", "Sydney", "Tokyo", "London", "New York")
for i , j in enumerate(cities):
    print(f"position {i} = {j}")

# cities[0]="delhi". tuples cannot be modified
# print(cities)

# In Machine Learning you will have data that should never be modified — like column names of a dataset, or fixed configuration values. Tuples protect that data from accidental changes.