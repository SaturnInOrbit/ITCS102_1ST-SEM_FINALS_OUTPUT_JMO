ans = 1
facto = eval(input("Enter a number you want to factorial: "))
for x in range(facto, 0, -1):
	print(x)
	ans *= x
print(f"The factorial of {facto} is {ans}")