# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Enter a 2 digit nnumer")

first_char = int(two_digit_number[0])
second_char = int(two_digit_number[1])
sum = first_char + second_char

print(type(first_char))
print(first_char)

print(str(first_char) + " + " + str(second_char) + " =" + str(sum))