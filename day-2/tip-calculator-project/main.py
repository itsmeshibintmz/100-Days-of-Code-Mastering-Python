print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

bill_new = bill + (bill * tip_percentage / 100)
each_person_pay = float(bill_new / people)
each_person_pay_round = round(each_person_pay,2)

print(f"Bill to pay per each person: {each_person_pay}" )