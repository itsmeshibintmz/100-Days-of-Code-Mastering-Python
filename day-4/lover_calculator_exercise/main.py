print("Welcome to Love Calculator!")

first_name = input("Enter your name: ")
second_name = input("Enter your crush's name: ")

len_first = len(first_name)
len_second = len(second_name)

count_first_name = 0
count_second_name = 0

for len_first in first_name:
    if i == "T" or i == "R" or i == "U" or i == "E" or i == "t" or i == "r" or i == "u" or i == "e":
        count_first_name += 1
for i in len_second:
    if i == "T" or i == "R" or i == "U" or i == "E" or i == "t" or i == "r" or i == "u" or i == "e":
        count_second_name += 1

print(count_first_name)