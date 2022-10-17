height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = int(weight / (height ** 2))

# print(type(bmi))
if bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")
    if bmi < 35:
        print(f"Your BMI is {bmi}, you are obese.")
    elif bmi < 30:
        print(f"Your BMI is {bmi}, you are slightly overweight.")
    elif bmi < 25:
        print(f"Your bmi is {bmi}, you have a normal weight.")
else:
    print(f"Your bmi is {bmi}, you are underweight.")
        



"""
"Your BMI is 18, you are underweight."
"Your BMI is 22, you have a normal weight."
"Your BMI is 28, you are slightly overweight."
"Your BMI is 33, you are obese."
"Your BMI is 40, you are clinically obese."
"""