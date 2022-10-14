# print(8 / 3)
# print(int(8 / 3))

# to round the number

print(round(8 / 3))
# = 3 (2.6666666666666665)

# we can specify the no.of digits of precision you want to round to

print(round(8 / 3, 2))
# = 2.67

print(type(8 // 3)) # = 2 without converting to int

result = 4 / 2

result /= 2

print(result)

# +=, -=. /=, *= 

# F strings
#----------

score = 0
height = 1.8
isWinning = True

# f-string
# adding and f" or f' in front of the string

print(f"Your score is {score}, your height is {height}, and you are winning is {isWinning}")