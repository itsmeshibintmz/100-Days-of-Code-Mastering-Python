# Nested if else

"""
if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this
"""

# print("Welcome to the rollercoaster")

# height = int(input("What is your height in cm? "))
# age = int(input("What is your age? "))

# if height >= 120:
#     print("You can ride the rollecaster!")
#     if age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("You can't ride the rollercoaster!")

# eif


"""
if condition1:
    do A
elif condition2:
    do B
else:
    do this
"""

print("Welcome to the rollecaster!")

height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    print("You can ride the rollecaster!")
    if age < 12:
        print("Please pay $5.")
    elif age <=18:
        print("Please pay $7..")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you can't ride the rollecaster!")