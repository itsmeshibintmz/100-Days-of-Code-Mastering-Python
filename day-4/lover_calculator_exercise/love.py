print("Welcome to the Love Calculator!");

name1 = input("What is our name?: ");
name2 = input("What is their name?: ");

combinedString = name1 + name2
lowerCaseString = str.lower(combinedString)

# print(lowerCaseString)

countTrue = 0

countTrue += lowerCaseString.count("t")
countTrue += lowerCaseString.count("r")
countTrue += lowerCaseString.count("u")
countTrue += lowerCaseString.count("e")

countLove = 0

countLove += lowerCaseString.count("l")
countLove += lowerCaseString.count("o")
countLove += lowerCaseString.count("v")
countLove += lowerCaseString.count("e")

print(countTrue)
print(countLove)
# print(type(countLove))

loveScore = int(str(countLove) + str(countLove))

print(loveScore)

if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <= 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")