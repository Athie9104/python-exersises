# Exercise 1
"""grades = [20, 10, 90, 85, 40, 75, 65, 64, 12, 74, 71, 98, 50]
for x in grades:
    if x >= 70:
        print(x)"""

# Exercise 2
"""dog_ages = [12, 8, 4, 1, 2, 6, 4, 4, 5]
for i in dog_ages:
    dog_years = i * 7
    print(dog_years)"""

# Exercise 3
# import math
transactions = [51.0, 49.99, 80.99, 67.99, 120.52, 23.49]
# Converting to a whole number
convert_to_single_total = [round(num) for num in transactions]
# Printing converted list
print("Converted transactions ", convert_to_single_total)
