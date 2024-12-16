def factorial():
    factorial = 1
    start = eval(input("enter the number you want to factorial: "))
    for x in range(start,0,-1):
        print(x)
        factorial *= x
    print(f"the factorial of {start} is {factorial} ")