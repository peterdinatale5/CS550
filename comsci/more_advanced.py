##### Problem 1
import sys

print("\nThis program will display the wind chill.")

t = float(sys.argv[1]) #storing the numbers entered in command line
v = float(sys.argv[2])

if (abs(t) < 50) or (v > 120 or v < 3): # a satement to ensure the ranges of t and v are suitable
	print("invalid input")
else:
	w = 35.74 + (0.6215*t) +((0.4275*t)-35.75)*v**0.16 #wind chill
	print(f"The wind chill is {w}") #formatted string

##### Problem 2
import sys

x = float(sys.argv[1]) #storing the numbers entered in command line
y = float(sys.argv[2])
z = float(sys.argv[3])

result = (x < y and y < z) or (x > y and y > t)
print(result) #return a boolean either True or False depending on if the numbers satisfy the above statement

# ##### Problem 3
import sys

days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'] #array for storing days

m = float(sys.argv[1]) #storing the numbers entered in command line
d = float(sys.argv[2])
y = float(sys.argv[3])

y_0 = y - int((14 - m) / 12) #formulas for determining day in Gregorian Calendar
x =   y_0 + int(y_0/4) - int(y_0/100) + int(y_0/400)
m_0 = m + 12 * int((14 - m) / 12) - 2
d_0 = int(d + x + (31*m_0) / 12) % 7

print(f"The day of the week is {days[d_0]}") #formatted string to display day of week

'''
Everytime division occurs, you must take the integer of the
result so you aren't working with a decimal.
'''

'''
Code can be executed by commenting out all other code.
on my honor, I have niether given nor recieved unauthorized aid. 
Peter DiNatale
'''
