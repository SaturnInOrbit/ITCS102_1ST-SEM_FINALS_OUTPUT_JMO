def act2():
    name = input("Please enter a name! ---> ")
    print("sup " + name)

def act4():
    number1 = eval(input("Enter a number: "))
    number2 = eval(input("Enter a second number: "))
    answer = number1 + number2
    print("The sum of" , number1 , "and" , number2 , "is" , answer)

def act5():
    print("Farenheit to Celsius Converter Program!")
    fahrenheit = eval(input("Please enter temperature in Farenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("The conversion of" , fahrenheit , "degrees Fahrenheit is" , round(celsius,2) , "degrees Celcius!")

def act6():
    x = 5

    print(x)

    x = x + 10

    print(x)

    x = x + 15

    print(x)

    x += 20
    print(x)

    x -= 25
    print(x)

def act8():
    password = input("Please enter a password ----> ")
    if password.lower() == "secret066":
        print("May tama ka!")
        print("Enjoy your 30 minutes of free browsing with SMART Prepaid!")
    elif password == "jamesorte":
        print("Well tama rin")
        print("Enjoy your 30 minutes of free browsing with SMART Prepaid!")
    else:
        print("Nope, try again")

    print("Thank you for choosing Globe, as your number one service provider")

def act10():
    isDLL = input("Are you currently enrolled ni DLL?(Y/N): ")
    if isDLL.lower() == "y":
        isIYAM = input("Do you currently live in Brgy. Ibabang Iyam?(Y/N): ")
        if isIYAM.lower() == "y":
            print("Welcome! Please confirm your school year")
            isSY = input("Please enter your current year level in DLL:\nF - Freshman\nS - Sophomore\nJ - Junior\nR - Senior\n")
            if isSY.lower() == "f":
                print("Hi Freshman!")
            elif isSY.lower() == "s":
                print("Hi Sophomore!")
            elif isSY.lower() == "j":
                print("Hi Junior!")
            elif isSY.lower() == "r":
                print("Hi Senior!")
            else:
                print("Invalid year level, please try again")
            isScho = input("Do you need this scholarship?(Y/N): ")
            if isScho.lower() == "y":
                print("You have been granted a full scholarship, thank you for choosing DLL")
            else:
                print("Okay, have a nice day")
        else:
            print("Sorry, you are not eligible")
    else:
        print("Sorry, you are not eligible")

def act11():
    for ulit in range(1,11):
        print("Hello World")

def act12():
    for ikot in range(10,1,-1):
        print(ikot)

def act13():
    start = eval(input("enter the number you want to factorial: "))
    factorial = 1
    for x in range(start,0,-1):
        print(x)
        factorial *= x
    print(f"the factorial of {start} is {factorial} ")

def act14():
    for x in range(0,11):
        print(x, end = " ")
        for y in range(0,11):
            print(" *", end ="")
        print()

def act15():
    for x in range(0,10):
        print(x, end=" ")
        for y in range(0,x):
            print(" *", end ="")
        print()
    for x in range(10,-1,-1):
        print(x, end = " ")
        for y in range(x,0,-1):
            print(" *", end ="")
        print()

    
Tuloy = True
while Tuloy == True:
    act = input("What activity would you like to try?(2/4/5/6/8/10/11/12/13/14/15/stop): ")
    if act == "2":
        act2()
        continue
    elif act == "4":
        act4()
        continue
    elif act == "5":
        act5()
        continue
    elif act == "6":
        act6()
        continue
    elif act == "8":
        act8()
        continue
    elif act == "10":
        act10()
        continue
    elif act == "11":
        act11()
        continue
    elif act == "12":
        act12()
        continue
    elif act == "13":
        act13()
        continue
    elif act == "14":
        act14()
        continue
    elif act == "15":
        act15()
        continue
    elif act.lower() == "stop":
        break
    else:
        print("wala naman sa pamimilian yan, ulit")
        continue
