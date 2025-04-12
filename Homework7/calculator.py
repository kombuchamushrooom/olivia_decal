import math_tools as matpy

a = float(input("Enter the first number: "))

str = str(input("Enter +,-,*, or /"))

b = float(input("Enter the second number: "))


if str == "+":
	print(matpy.add(a, b))

elif str == "-":
	print(matpy.subtract(a,b))

elif str == "*":
	print(matpy.multiply(a,b))

elif str == "/":
	print(matpy.divide(a,b))

else:
	print("Calculator does not recognize this operation, try again")

