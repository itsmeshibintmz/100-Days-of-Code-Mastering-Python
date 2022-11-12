print("Welcome to rollercoaster!")

height = int(input("What is your height in cm ?"))
age = int(input("What is your age ?"))
bill = 0

if height >= 120:
    print("You can ride the rollecoaster!")
    if age < 12:
        bill += 5
    elif age >= 12 & age < 18:
        bill += 7
    else:
        bill += 12
    print(f"Your bill is {bill}")
else:
    print("Sorry, you can't ride the rollercoaster!")
