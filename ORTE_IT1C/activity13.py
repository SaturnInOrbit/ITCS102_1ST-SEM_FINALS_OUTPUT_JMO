start = eval(input("enter the number you want to factorial: "))
factorial = 1
for x in range(start,0,-1):
    print(x)
    factorial *= x
print(f"the factorial of {start} is {factorial} ")