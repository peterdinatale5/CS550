import sys


# num = int(input("Enter a number: "))
# result = num % 10 <= 2 or num % 10 >= 8
# print(result)

# num1 = int(sys.argv[1])
# num2 = int(sys.argv[2])
# result1 = num1//num2 == num1/num2
# result2 = num2//num1 == num2/num1
# result = result1 or result2
# print(result)

num1 = int(sys.argv[1])
result = (num1%4 == 0)
print(result)