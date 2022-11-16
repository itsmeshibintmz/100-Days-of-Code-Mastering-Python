print("Welcome to the Love Calculator!")

name1 = input("What is your name?: ")
name2 = input("What is  their name?: ")

count = 0

for char in name1:
    if char == "T" or char == "R" or char == "U" or char == "E" or char == "t" or char == "r" or char == "u" or char == "e":
        count += 1

for char in name2:
    if char == "T" or char == "R" or char == "U" or char == "E" or char == "t" or char == "r" or char == "u" or char == "e":
        count += 1

print(count)