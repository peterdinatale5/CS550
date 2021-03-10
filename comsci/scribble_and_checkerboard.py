# from PIL import Image, ImageDraw
# import random
# import math

# imgX = 200
# imgY = 200
# image = Image.new("RGB",(imgX, imgY))

# def scribble():
# 	g = random.randint(0,255)
# 	r = random.randint(0,255)
# 	b = random.randint(0,255)
# 	x = random.randint(2,200)
# 	y = 1

# 	while y < 200 and x > 0 and x < 200:
# 		image.putpixel((x,y),(r,g,b))
# 		rand = random.randint(1,5)
# 		if rand == 1:
# 			x += 1
# 		elif rand == 2:
# 			x -= 1
# 		else:
# 			y += 1

# 	image.save("demo.png", "PNG")

# for x in range(10):
# 	scribble()


# #Ignore
# #(checkerboard code from class)
# def checkerboard():
# 	for w in range(0,500,100):
# 		for h in range(0,500,100):
# 			for x in range(w, w+50):
# 				for y in range(h, h+50):
# 					g = 50
# 					r = 0
# 					b = 50
# 					image.putpixel((x,y),(r,g,b))

# 	for w in range(0,500,100):
# 		for h in range(0,500,100):
# 			for x in range(w+50, w+100):
# 				for y in range(h+50, h+100):
# 					g = 50
# 					r = 0
# 					b = 50
# 					image.putpixel((x,y),(r,g,b))

# 	image.save("demo.png", "PNG")




	#new assignment



# Create a list of 5 different grades. If the grade is above or equal to 50, print "you passed." Otherwise, they failed!

grades = [50, 89, 20, 44, 90]

for grade in grades:
	if grade >= 50:
		print(f"Your grade is {grade} You Passed")
	else:
		print(f"Your grade is {grade} You Failed")












