print("Welcome to rollercoaster!")

height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollecoaster!")

    age = int(input("What is your age? "))
    want_photo = input("Do you want a photo as a memory? Y or N? ")

    if want_photo == "Y":
        bill += 3
        
    if age >= 45 and age <= 55:
        bill = 0
        print(f"Your bill is ${bill}")
        print("Enjoy your ride.")
    elif age < 12:
        bill += 5
    elif age >= 12 & age < 18:
        bill += 7
    else:
        bill += 12

    print(f"Your total bill is ${bill}")
    print("Enjoy your ride.")

else:
    print("Sorry, you can't ride the rollercoaster!")

