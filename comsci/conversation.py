
#this is a program that will have a conversation with the user

print("\nHi there! My name is Peter, and I am a senior at Choate.\nI am also 18 years old ——— ", end="")

name = input("What is your name? ")
age = int(input("Hello, "+name+"! Nice to meet you.\nHow old are you? "))
next_age = age + 1

age_response = input("Sweet, when will you turn " +str(next_age)+ "? ")
location = input("Cool, and where are you from? ")
pet = input("Nice! I love that place! Do you like cats? They are my favorite pet. (Yes or No) ").lower()

if pet == "yes":
	print("Awesome! I really love cats.")
else:
	input("You should considering liking them because they are a great pet. What is you favorite pet? ")
	print("Hey thats pretty cool!")


print("\nWell, it was nice to meet you! Take care!")

#end of the program

#on my honor, I have niether given nor recieved unauthorized aid. Peter DiNatale