print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
bill = 0

if height >= 120:
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12
    
    wants_photo = input("Do you want a photo taken? yes or no: ")
    if wants_photo == "yes":
        bill += 3
    
    print(f"Your bill is {bill}")
else:
    print("You can't ride the rollercoaster!")
