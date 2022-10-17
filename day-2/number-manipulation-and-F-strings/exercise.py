# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.
# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

age = int(input("Enter your age: "))

days_left = (90 * 365) - (age * 365)
weeks_left = (90 * 52) - (age * 52)
months_left = (90 * 12) - (age * 12)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

# atlernative answer

# age = input("what is your current age: ")

# age_as_int = int(age)

# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12

# message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months"
# print(message)
