'''
Peter DiNatale
01-25-2020

Sources:
- DATA I RESEARCHED
household size: https://www.statista.com/statistics/242189/disitribution-of-households-in-the-us-by-household-size/
commercially produced food data: 
(1) https://www.thesimpledollar.com/save-money/dont-eat-out-as-often/#:~:text=The%20average%20American%20eats%20an,month%20eaten%20outside%20the%20home.
(2) https://www.kinetic12.com/newsroom/consumer-fee-comparison-food-delivery-companies/#:~:text=Many%20consumers%20have%20come%20to,a%20service%20fee%20as%20well
age group calorie consumption: https://www150.statcan.gc.ca/n1/pub/82-620-m/2006002/c-g/4144191-eng.htm
socioeconomic status breakdown: https://www.pewresearch.org/fact-tank/2020/07/23/are-you-in-the-american-middle-class/
- SLIDESHOW IMAGES
Fast Food: https://logodix.com/fast-food-restaurants
Miniwheats: https://www.target.com/p/original-frosted-mini-wheats-breakfast-cereal-24oz-kellogg-s/-/A-12935208
grocieries: https://midwestcommunity.org/shop-best-deals-groceries/
Mccormic spices: http://www.walletwhisperer.com/saving-money-buying-seasonings/
- CODE REFERENCES
matplotlib documentation: https://matplotlib.org/

Summary of Process: When I first began this project, I started by generating a list of factors that I would need to calculate my own family's total spending
on groceries in a given year. I wrote out each of the factors, most of which I included in this program. Next, I asked myself how these facotrs could potentially change
the outcome of the overall results. For example, I took into account the fact that families will eat takeout, so I tried to calculate this value and subtract it from the overall cost of groceries.
To accurately repreent this scenario, I needed to search for delivery fees, average takeout prices, and frequency of orders per week. This is just one example of the five main factors I took
into consideration. I also found the feedback from Ms. Healey very helpful, such as including snacks in the meal, and pointing out the socioeconommic status doesn't
always correspond with one's choice of brand, for example. I either implemented these into the code or disussed them in my reflections slide. Overall, although this project did take a while
to complete, I defintely learned a lot about simulations, weighted randomness, and the best ways to accurately and fully represent data.

- 
Honor Code: "On my honor, I have niether given nor recieved unauthorized aid." - Peter Di Natale
'''

#LIBRARIES
import random
import matplotlib.pyplot as plt
import numpy as np

#CLASSES
class Family():
	'''
	A class to represent different attributes of a family; this class will be used in a for loop of 10,000 iterations. Each 'family' generated will
	be a unique representation of an average american household.
	'''
	def __init__(self, members, meal_cost, takeout, status):
		#constructor function that initializes the variables below, which will be used in the class later on
		self.members = members #number of members
		self.meal_cost = meal_cost #meal cost (single meal)
		self.takeout = takeout #takeout/ restaurant meal cost (single meal)
		self.status = status #status of family

	def status_mult(self):
		'''
		status multiplier - this function scales up meal price according to a person's
		socioeconomic status. I understand that there is also a flaw to this system, which is
		that people don't always buy brands with prices that correspond with their status. I tried
		account for this by not making the multiplier's effect too significant.
		'''
		global multiplier

		if self.status[0] == lis_status[0]:
			multiplier = 0.95
		elif self.status[0] == lis_status[1]:
			multiplier = 1.00
		elif self.status[0] == lis_status[2]:
			multiplier = 1.05
		return multiplier

	def age_calc(self):
		'''
		Calculating the age of the person and scaling up the cost of the meal
		The prices of meals depend on how old the person is. For example, a toddler's meal
		will cost much less than a hungry and growing teenager.

		The variable "total cost" tells us how much it costs to feed a given household 
		for one meal, taking into account how many meals need to be served (also known as number of family members) and the age of each member
		'''
		total_cost = 0 #see details above for this variable
		start = 0#variable to keep track of place in list of meals
		ages = [] #list of all the ages for members in the family
		meals = [self.meal_cost[0] for x in range(self.members[0])] #creating a list to store meal prices based on age.
		ages.clear()

		if (self.members[0]) == 1: #if the size of the family is 1 member, then this member is an adult
			ages.append(random.randint(25,90)) #choosing a random age for the adult
		elif (self.members[0]) > 2: #if the size of the family is more than 2 memebers
			for x in range(2):
				ages.append(random.randint(25,90)) #choose the ages of the parents
			for x in range(self.members[0]-2):
				ages.append(random.randint(1,24)) #choose the ages of the kids
		else: #if the size of the household is 2
			ages.append(random.randint(0,90))
			if ages[0] > 25: #if the family has an adult, then choose another age 0,90
				ages.append(random.randint(0,90))
			else: #if the 2 person family does not have an adult, then add one
				ages.append(random.randint(25,90))


		for age in ages: 
			#scaling meal costs based on the age group of the individual; I referred to the graph in the slide show for this
			if age > 0 and age <= 4:
				meals[start] *= 0.7
			if age > 4 and age <= 8:
				meals[start] *= 1.0
			elif age > 8 and age <= 14:
				meals[start] *= 0.7
			elif age > 14 and age <= 24:
				meals[start] *= 1.5
			elif age > 24 and age <= 64:
				meals[start] *= 1.2
			elif age > 65:
				meals[start] *= 0.8
			start += 1

		for meal in meals:
			total_cost += meal

		return (total_cost) #return the meal cost; this will be used in the end calucation that takes into account other factors

	def calculate_week_cost(self):
		'''
		function that calculates the total weeks cost, taking into account
		the number of members, the ages of members, and then subtracting the 
		takeout/commercially produced meal cost. The status muliplier comes in lateron
		when the meal cost is multiplied.
		'''
		global week_cost
		restaurant_meal_prices = [] #used for storing the restaurant prices
		meal_min_cost = 5 #the minimum for choosing the price of a commericially produced meal
		meal_max_cost = 25 #the maximum for choosing the price of a commercially produced meal

		for i in range(0,15):
			price = random.randint(meal_min_cost, meal_max_cost) 
			restaurant_meal_prices.append(price)

		week_cost = (21 * random_family.age_calc()) - random.choice(restaurant_meal_prices) #calculating the total amount spent in a given week for a selected family.

		return week_cost

#FUNCTIONS
def hist_point(grocery_price_range, graph_type):
	'''
	creating ranges for cost of groceries that will be used in the graphs. Each increase in a letter 
	represents a household that falls into respective price range (for annual grocery cost) 
	there are two parameters to this function, both of which help distinguish the "zoom" of the graph
	'''
	a,b,c,d,e,f,g,h = 0,0,0,0,0,0,0,0

	for i in avg_count:
		if i >= (grocery_price_range * 0.0) and i < (grocery_price_range * 0.5):
			a += 1
		elif i >= (grocery_price_range * 0.5) and i < (grocery_price_range * 1):
			b += 1
		elif i >= (grocery_price_range * 1) and i < (grocery_price_range * 1.5):
			c += 1
		elif i >= (grocery_price_range * 1.5) and i < (grocery_price_range * 2):
			d += 1
		elif i >= (grocery_price_range * 2.0) and i < (grocery_price_range * 2.5):
			e += 1
		elif i >= (grocery_price_range * 2.5) and i < (grocery_price_range * 3.0):
			f += 1
		elif i >= (grocery_price_range * 3.0) and i < (grocery_price_range * 3.5):
			g += 1

	if graph_type == "big":  #creating list for the zoomed out histogram
		hist_big = [a,b,c,d,e,f,g]
		return hist_big

	elif graph_type == "small": #creating list for the zoomed in histogram
		hist_small = [b,c,d,e,f,g]
		return hist_small


def create_graphs():
	'''
	Function that creates the two graphs shown when the program is run
	I did some researching in the mat plot lib documentation to figure out how to create two graphs, and I found
	that the proper way to do it was by using "subplot", So each subplot represents of different graph of the figure
	that is created with plt.figure()
	'''
	plt.figure() #creating a figure for the two graphs to be included in

	plt.subplot(211) #211 (and 212 in the next graph) which is passed into "sublot" is a three digit number used for positioning of the graph
	plt.xlabel('Cost of Groceries (intervals of $2.5k from 0 to $17.5k) ') #x axis label
	plt.ylabel('Number of Families') #y axis label 
	plt.title('Annual Costs of Groceries for 10,000 Families')
	plt.bar(["a","b","c","d","e","f","g"], hist_point(5000, "big"))

	plt.subplot(212)
	plt.xlabel('Cost of Groceries (intervals of $1k from 1k to $7k)') #x axis label
	plt.ylabel('Number of Families') #y axis label 
	plt.title('Annual Costs of Groceries for 10,000 Families')
	plt.bar(["a","b","c","d","e","f"], hist_point(2000, "small"))

	plt.show()

#VARIABLES
lis_members = [1,2,3,4,5,6,7] #list of possible numbers of members in a household
lis_meal_cost = [2.5, 3.0, 3.5, 4.0, 4.5] #list of possible meal prices
lis_takeout = [3, 4, 5, 6] #list of possible number of times a household will consume takeout
lis_status = ["lower", "middle", "upper"] #list of different status identifiers, used as a multiplier

iterations = 10000 #how many times the program is run
week_cost = 0 #used in the calculate week cost function to calculate the total amount spent in a given week for a selected family.
multiplier = 0 # variable used for scaling of upper, middle, and lower class
avg_count = [] #variable used to calculate costs by keeping possible values in a list

#MAIN CODE
for x in range(iterations):
	#lines that control weighted randomness of the varibale lists in the VARIABLES section
	#the weights below correspond with the values place in each of the "lis" variables
	members = random.choices(lis_members, weights=(28, 35, 15, 12, 6, 2, 1), k=1) #weights for members
	meal_cost = random.choices(lis_meal_cost, weights=(20,40,40,20,10), k=1) #weights for meal cost
	takeout = random.choices(lis_takeout, weights=(10, 40, 40, 10), k=1) #weights for number of commercially produced meals
	status = random.choices(lis_status, weights=(29,52,19), k=1) #weights for status/class

	random_family = Family(members, meal_cost, takeout, status) #creating a family with the given parameters that use the weights above
	avg_count.append((random_family.calculate_week_cost() * random_family.status_mult())*52) #multiplying by 52 because there are 52 weeks in a year
	single_price = (sum(avg_count)/10000) #finding the sum of all the prices to arrive at an average (divide by 10,000)

print(hist_point(5000, "big")) #printing the lists just for testing purposes
print(hist_point(2000, "small"))
print(f"The average household's annual grocery cost is {single_price}") #finding the sum of all the prices to arrive at an average (divide by 10,000)
create_graphs()








