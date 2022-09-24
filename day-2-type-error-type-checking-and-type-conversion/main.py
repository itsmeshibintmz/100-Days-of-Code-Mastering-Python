# len(123) # Type Error

# num_char = len(input("what is your name? "))
# # print("Your name ha " + num_char + " characters") # TypeError: can only concatenate str (not "int") to str

# # print(type(num_char)) # type function

# # Type Conversion

# new_num_char = str(num_char)

# print("Your name has " + new_num_char + " characters")

'''
output
what is your name? shibin
<class 'int'>
Your name has 6 characters
'''

a = str(123)
print(type(a))

print(70 + float("100.5"))

# 170.5

print(str(70) + str(100))

# 70100