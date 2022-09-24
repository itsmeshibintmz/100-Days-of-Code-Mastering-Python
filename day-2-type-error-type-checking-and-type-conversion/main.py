# len(123) # Type Error

num_char = len(input("what is your name? "))
# print("Your name ha " + num_char + " characters") # TypeError: can only concatenate str (not "int") to str

print(type(num_char)) # type function

# Type Conversion

new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters")
