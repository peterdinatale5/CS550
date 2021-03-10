'''
Peter Di Natale
Recursion Homework
10-15-2020

Source: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
Note: I used this source to gain basic background information regarding the algorithm

Towers of Hanoi:
Note: I had some trouble figuring out what certain parts of the program meant, but here is an attempt at explaining what I understood.
Some confusions: 
- Is n the disc number or the number of discs? I assumed the disc number.
- Why are the two instances of recursion not indented? And why must they run twice?

Trace:
create a function that takes in the variables "n" and left, a boolean
if the disc number is 0, go through the function again, but this time with n-1 as the disc number and left as false
if left is true, print the disc number as a string and "left"
if left is false, print the disc number as a string and "right"
go through the function again, but this time with n-1 as the disc number and left as false

Explanation:
ultimalely, this program should give the directions on how to solve the towers of hanoi
this function first takes in two parameters: the disc number and left as a boolean, in orther words the direction that the disc needs to be moved
if the function moves the disc to the right, left is false, so the else condition will run
if the function moves the disc to the left, left is true, and the "if left condition will run.
the program will keep repeating itself with parameters n and boolean left until the game is completed.
'''

print("Welcome to GCD! Enter two numbers to find their greatest common denominator")
x_num = int(input("X: "))
y_num = int(input("Y: "))

def gcd(x, y):  
    if (x == 0): 
        return y 
    elif (y == 0):
    	return x 
    else:
	    return gcd(y%x, x%y)

print(gcd(x_num,y_num))








