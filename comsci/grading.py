'''
Peter Di Natale
09-15-2020
Desc: Grading Program
Sources: None
'''

import sys

x = float(sys.argv[1])

if x >= 4.67 and x <= 5:
	print("A+")
elif x >= 4.33 and x < 4.67:
	print("A")
elif x >= 4 and x < 4.33:
	print("A-")
elif x >= 3.67 and x < 4:
	print("B+")
elif x >= 3.33 and x < 3.67:
	print("B")
elif x >= 3 and x < 3.33:
	print("B-")
elif x >= 2.67 and x < 3:
	print("C+")
elif x >= 2.33 and x < 2.67:
	print("C")
elif x >= 2 and x < 2.33:
	print("C-")
elif x >= 1.67 and x < 2:
	print("D+")
elif x >= 1.33 and x < 1.67:
	print("D")
elif x > 1 and x < 1.33:
	print("D-")
elif x <= 1:
	print("F")

else:
	print("I am looking for a number between 0 and 5, sorry!")
	quit()

print("Welcome to the fortune teller!")

age = int(input("what is your age: "))
food = input("what is your favorite food: ")
home = input("what town do you live in: ")

print(f"\nIn 5 years, you will be {age + 5}, you will live in a mansion not in {home}, but rather in Alaska.\nYou will also obtain a lifetime supply of {food}.\n")




#below is code/notes from class; ignore

# ####
# isWindy = False
# isRaining = True

# if isRaining and not isWindy:
# 	print("bleh")
# elif isRaining and isWindy:
# 	print("no")

# try:
# 	age = int(input("what is your age"))

# except ValueError:
# 	age = int(input("what is your age"))


# if age < 10:
# 	("horrah you are young")
# elif age >= 10 and age <= 20:
# 	("you are getting old")
# else:






