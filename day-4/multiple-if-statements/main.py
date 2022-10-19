# if/ elif / else

# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do C

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    print("you can ride the rollercoaster!")
    wants_photo = input("Do you want a photo taken? yes or no: ")
    
    if age >= 18:
        if wants_photo == "yes":
            print("you need to pay an extra of $15")
        else:
            print("you need to pay an extra of $12")
    elif age >= 12 and age < 18:
        if wants_photo == "yes":
            print("you need to pay an extra of $10")
        else:
            print("you need to pay an extra of $7")
    elif age < 12:
        if wants_photo == "yes":
            print("you need to pay an extra of $8")
        else:
            print("you need to pay an extra of $5")
else:
    print("you can't ride the rollercoaster!")
