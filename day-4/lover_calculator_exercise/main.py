print("Welcome to the Love Calculator!")

name1 = input("What is your name?: ")
name2 = input("What is  their name?: ")

countTrue = 0
countLove = 0

for char in name1:
    if char == "T" or char == "R" or char == "U" or char == "E" or char == "t" or char == "r" or char == "u" or char == "e":
        countTrue += 1

for char in name2:
    if char == "T" or char == "R" or char == "U" or char == "E" or char == "t" or char == "r" or char == "u" or char == "e":
        countTrue += 1

for char in name1:
    if char == "L" or char == "O" or char == "V" or char == "E" or char == "l" or char == "o" or char == "v" or char == "e":
        countLove += 1

for char in name2:
    if char == "L" or char == "O" or char == "V" or char == "E" or char == "l" or char == "o" or char == "v" or char == "e":
        countLove += 1

print(countTrue)
print(countLove)

# print(type(countTrue))

count = int(str(countTrue) + str(countLove))

print(count)
""" if countTrue < 40 :
    print(f"Your score is {count}.")
elif count
"""