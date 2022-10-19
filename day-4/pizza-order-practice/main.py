# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.
# Small Pizza: $15, Medium Pizza: $20, Large Pizza: $25, Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3, Extra cheese for any size pizza: + $1

print("Welcome to Pizza Hub!")

size = input("Which size pizza you want? S for Small, M for Medium or L for Large: ")
add_pepperoni = input("Do you want to add pepperoni? Y or N:")
bill = 0

if size == "S" and add_pepperoni == "Y":
    bill += 17
elif size == "S" and add_pepperoni == "N":
    bill += 15
elif size == "M" and add_pepperoni == "Y":
    bill += 23
elif size == "M" and add_pepperoni == "N":
    bill += 20
elif size == "L" and add_pepperoni == "Y":
    bill += 28
elif size == "L" and add_pepperoni == "N":
    bill += 25

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1
else:
    bill += 0

print(f"Your total bill for the pizza is: {bill}")
