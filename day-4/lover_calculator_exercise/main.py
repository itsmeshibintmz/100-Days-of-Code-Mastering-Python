print("Welcome to Love Calculator!")

first_name = input("Enter your name: ")
second_name = input("Enter your crush's name: ")

count = 0

for char in first_name:
    if char == "T":
        count += 1

for char in second_name:
    if char == "T":
        count += 1

print(count)