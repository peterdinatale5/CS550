#text game
'''
Peter Di Natale
09-17-2020
Description: This is a user interaction program that is composed of three mini adventures/encounters.
				I wanted each one to be unique and pretty random to add some humor to the game. The user
				can pass through adventures three times, choosing either to complete all adventures, or repeat
				one if they want. After each mini adventure, the user returns to "home base" where they can choose
				their next adventure. After the third time around, the game finishes. 

				In terms of the process for coding this game, I started off the program with three functions,
				one for each mini adventure. I did this mainly to keep my different mini-adventures organized.
				Along the way, I had some trouble referencing certain variables across different functions,
				so I did some research to figure out the best way to approach this problem. Additionally, in order to ease testing,
				I commented out different portions of the code as I was trying out different ideas. This allowed me to
				more effectivly locate any issues without having to pass through the entire game.
Sources: 
https://stackoverflow.com/questions/11904981/local-variable-referenced-before-assignment (question on global vs local variable)
https://docs.python.org/3/library/time.html (I used this to create delays to add suspense in the program)
Honor Code: On my honor, I have niether given nor recieved unauthorized aid. Peter Di Natale

#note: no sections of my code have been borrowed from external sources.
'''

#import
import random as r #library that will be used in order to generate random values/things
import time #library that I will use to generate pauses to add suspense to the game

#functions
def greet():
	'''
	This function serves to welcome the user in the first part by collecting their name as a variable
	Farther down is a try and except statement that collects the users age. If the user doesn't enter a number, 'except' will run
	The age is also stored in a variable, as it will be used later on.
	The home location of the user is the last input and is stored in home, which will be referenced later.

	'''
	global user_name #(making these variables global so I can access them outside of their home.)
	global age
	global home
	global ishome
	print("\nWelcome to the triple mini-adventure game! This game is composed of three mini-adventures: forest, mountain, and city. Each one is unique!")
	user_name = input("What is your name? ")
	print("\nHello, "+user_name+"! You have three tickets to travel. On each trip to a mini adventure, you will have a brief encouter with someone or something.") 
	print("Before you leave, I just have a few questions.")
	try: #(try and except incase the user doesnt enter a numberical value)
		age = int(input(f"How old are you? Please enter a number. ")) #try and accept here in case the user attempts to break the program by entering a string, for example
	except ValueError:
		print("\nYou are now 75 because you didn't enter a number 😡.")
		age = 75

	home = input("\nWhere do you live? ")
	print("\nThanks! Now enjoy the adventure!")
	time.sleep(1.5) #delay for suspense

def location():
	'''
	Throughout this function, there are if statements that are referencing the variable ishome.
	This variable increases each time a mini-adventure is finished. Therefore, depeding on the number of the varible, 
	the user will either have 2, 1, or 0 mini-adventures left. 

	There is also another set of if, elif, and else statements when ishome = 0.
	Here, the user will decide if they want to choose their destination or be randomly put into one.
	This function works a lot in conjunction with choose_game() to avoid repitiion of code.

	'''
	global response
	global ishome
	places = ['forest', 'city', 'mountain'] #an array that includes a list of places the user can choose from
	if ishome == 0:
		response = input(f"\nSooo {user_name}, would you like to choose your destination [c] or be assigned randomly [r]? (c/r) ").lower()
		if response == 'c':
			response = input(f"\nYour choices are {places}, which would you like? ").lower()
			choose_game()
		elif response == 'r': #destination will be random
			response = r.choice(places) #picks a random word in the array places
			choose_game()
		else:
			print("You did not enter correctly, so you will be assigned randomly.")
			response = r.choice(places) #picks a random word in the array places
			choose_game()
	if ishome == 1:
		print("Welcome back to home base.\nYou've completed one adventure. Which would one would you like to tackle next?\n")
		response = input(f"\nYour choices are {places}, which would you like? ").lower()
		choose_game()
	if ishome == 2:
		print("Welcome back to home base.\nYou are now onto your final game!")
		response = input(f"\nYour choices are {places}, which would you like? ").lower()
		choose_game()
	if ishome == 3:
		print("Welcome back to home base.\nThis is now your third time back, so congratulations on finishing the game! Have a great day.")
		time.sleep(2) #paused the program for suspense
		quit()

def choose_game():
	'''
	This is a function choosing which mini adventure to conquer
	As mentioned earlier, it works in conjunction with the user's inputs in the function above.
	Choose_game() is also called after the user finishes one adventure and enters the next one. 

	'''
	if response == 'forest':
		print("\nOff to the forest you go!")
		forest()
	elif response == 'city':
		print("\nOff to the city you go!")
		city()
	elif response == 'mountain':
		print("\nOff to the mountain you go!")
		mountain(bear_num) #bear_num variable passed in to function (random interger)
	else:
		print("Invalid response. Try again!")
		location()

def forest(): 
	'''
	This is the forest function that contains a mini adventure the user can enter
	In the farthest left intended series of if statements, the outcome depends on if the user wanted to talk or run from the animal
	I also used some f strings to to enter variables into strings throughout the function.
	'''
	global ishome 
	print("Welcome to the forest adventure.")
	animal = r.choice(['frog','duck','bear']) #an array of random animals that the user could possibly encounter
	name = r.choice(['fred', 'max', 'tim', 'jake']) #an array of random names for that animal
	animal_approach = input(f"\nAn {animal} appears. Do you run from [r] or talk to [t] the {animal} (r/t)? ").lower()
	if animal_approach == 'r':
		animal_approach = input("\nIt starts snowing heavily. Do you want a snow mobile to reach home base? (y/n)").lower()

		#in the three conditions below, inputs are in response to the snow that comes
		#the user will either be sent back to home base on a snowmobile or in a helicopter
		if animal_approach == 'y':
			print(f"Snowmobile headed your way shortly. Enjoy the ride!\n")
			ishome += 1
			return_home = True
		elif animal_approach == 'n':
			print("Unfortunately you froze in the snow and a helicopter returned you to home base.")
			ishome += 1
			return_home = True
		else:
			print("Sorry, that input is invalid. Try again!")
			forest()

	elif animal_approach == 't':
		print(f"The {animal}'s name is {name}. You tell {name} that you are lost and that you need help.")
		animal_approach = input('''\nDo you trust him? (y/n) He seems really nice! ''').lower()

		#these next conditions are if the user deicded to talk to the animal
		#in one of the functions, the user is sent to the city, but in this case, ishome does not increase, since the user didn't reach home base
		if animal_approach == 'y':
			print(f"Good choice, {name} led you back home.\n")
			ishome += 1
			return_home = True
		elif animal_approach == 'n':
			print("Ok then would you will be directed to the city. Have fun! \n")
			city()
		else:
			print("Sorry, that input is invalid. Try again!")
			forest()
	else:
		forest()

def city(): 
	'''
	This is the city function that contains another mini adventure
	The farthest left indented if, elif and else conditoins are outcomes based on what the used resonds the the very awkward cashier
	Based on the response, the user will enter into either more statements, return home, or repeat the function over again
	'''
	global ishome
	print("You are now in New York City. You are thirsty, so you enter a coffee shop to drink.")
	print(f"The cashier knows you, but you dont recognize him. He says, Hey!! {user_name}, you are that {age}-year-old from {home}! I know you!!")
	cashier_res = input("\nYou feel super awkward. Do you leave or stay (l/s)").lower() #initial input
	if cashier_res == 'l':
		print("Good choice, that was really wierd\n")
		ishome += 1
		return_home = True
	elif cashier_res == 's':
		cashier_res = input("\nYou order your coffee. The person waves goodbye to you. Do you wave back (y/n) ")
		if cashier_res == 'y':
			print("That was nice of you.\nYou realize that the man wasn't wierd after all...but how did he know you?\n")
			bus_walk = input("\nWould you like to walk or take the bus back to home base? (b/w)")
			#the following conditions will decide how the user gets home. this is if they waved to cashier.
			#if they don't wave to the cashier, they will be transported home.

			if bus_walk == 'b':
				print("Good choice! You made a friend on the bus and didn't get caught in the rain.\n")
				ishome += 1
				return_home = True
			elif bus_walk == 'w':
				print("You chose to walk back and it started raining. 🌧 ")
				ishome += 1
				return_home = True
			else:
				print("Sorry, that input is invalid. Try again!")
				city()
		else:
			print("Sorry, that input is invalid. Try again!")
			city()
	else:
		city() #repeat the function if the user fails to enter a valid input

def mountain(bears): #passed in 'bears' so when the random number is generated from bear_num, the for loop runs the print statement a certain number of times
	'''
	Mountain function - to start off the mini adventure, a for loop runs to create a bunch of bears that will hopefully scare the user.
	The user then has a chance to hug the bears. Their response is addressed in the main if, elif, else sequence in this function. (indented farthest left)
	Embedded inside this main sequence of conditions are more experiences that will prompt the user.

	'''
	global ishome
	print("You fall into the middle of a mountain, and you are very scrared. You search around for some food, but you have a hard time finding some.\nThen, all of a sudden, you notice something in the distance...")
	time.sleep(3.5) #paused the program for suspense preceding the bear ambush

	print("LOOK OUT! A surge of bears is coming at you!")
	for bear in range(bears): #print the statement for the number of times that was chosen in variable bear_num using random
		print("🐻 🐻 🐻 🐻 🐻 🐻 ") #bear emojis added for fun!

	bear_attack = input(f"\nDo you want to hug the bears (y/n)? ").lower() #initial input
	if bear_attack == 'n':
		print("You missed out on a hug from the friendly family of bears :( ")
		bear_attack = input("\nYou keep running and find meet a park ranger. He seems kind and trustworthy. Do you go with him? (y/n)").lower()
		#the conditions below are for the park ranger encounter that is mentioned above

		if bear_attack == 'y':
			print(f"Good choice, the park ranger led you back to home base.\n")
			ishome += 1
			return_home = True
		elif bear_attack == 'n':
			print("You were stranded in the city and end up dying.")
			quit()
		else:
			print("Sorry, that input is invalid. Try again!")
			mountain()

	elif bear_attack == 'y':
		print("The bears do not eat you! They give you a hug and carry you to home base.\n")
		ishome += 1
		return_home = True
	else:
		print("Sorry, that input is invalid. Try again!")
		mountain()

#variables
return_home = False #this boolean will become true each time I want the user to be sent back to the location function
ishome = 0 #this variable keeps track of the number of mini adventure the user completes. After 3, the game finishes
bear_num = r.randint(10,20) #this variable is used to generate a bear attack in the game

#main code
while True: #while loop that runs the game continuously
	greet()
	location()
	if return_home == True: # if this boolean is true, then return back to the location function
		location()


'''
Max: Give a more detailed description at the start so the user is more aware of the game
What did I do: I added to the description that was already there. I do agree with max that the description should be detailed because of the different parts that my game contains.

Grace L: Shorten the pauses that appear occasionally throughout the program a little bit because they can get confusing if too long.
What did I do: I shortened the pauses so they are not as long
I agree with grace theat got confusing after a while, and the suspenseful effect I'm looking for still works.

After playing the game a few time and reviewing feedback, I polished the code by ensuring no crashes occur;
adding comments to better communicate the functions and sections of functions; fixing stylistic elements such as grammer
and spelling; adding the variables to the bottom below all the functions; and lastly rearranging line breaks and putting them after inputs to make the text more readable.

'''
