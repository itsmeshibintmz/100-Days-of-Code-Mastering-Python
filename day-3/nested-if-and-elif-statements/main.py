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

print("Welcome to the rollercoaster")

height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    if age > 18:
        print("You can ride the rollecaster!")
        print("Please pay $12.")
    else:
        print("You can ride the rollercoaster!")
        print("Please pay $7.")
else:
    print("You can't ride the rollercoaster!")
