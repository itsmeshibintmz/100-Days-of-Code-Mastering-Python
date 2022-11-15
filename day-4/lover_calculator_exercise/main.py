print("Welcome to Love Calculator!")

first_name = input("Enter your name: ")
second_name = input("Enter your crush's name: ")

count = 0

for char in first_name:
    if char == "T" or char == "R" or char == "U" or char == "E" or char == "t" or char == "r" or char == "u" or char == "e":
        count += 1

for char in second_name:
    if char == "T" or char == "R" or char == "U" or char == "E" or char == "t" or char == "r" or char == "u" or char == "e":
        count += 1

print(count)