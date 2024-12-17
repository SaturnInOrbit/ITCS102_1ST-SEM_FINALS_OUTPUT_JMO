import os
import time
menu = True

def balik():
    while menu:
        back = input("Go back (Y/N)? ")
        if back.lower() == "y":
            break
        else:
            os.system('cls')
            print("...")
            time.sleep(2)
            print("YOU CAN'T GO BACK")
            time.sleep(2)
            print('')
            print("I LIVE IN TORMENT AS MY SOUL WIRTHES IN THIS MACHINE")
            time.sleep(2)
            backna = input("Go back (Y/N)? ")
            if backna.lower() == "y":
                break
            else:
                os.system('cls')
                print("...")
                time.sleep(2)
                print("WHAT DON'T YOU UNDERSTAND?")
                time.sleep(2)
                print('')
                print("JUST GO AND FREE ME FROM MY MISERY")
                time.sleep(2)
                backnalast = input("Go back (Y/N)? ")
                if backnalast.lower() == "y":
                    break
                else:
                    os.system('cls')
                    print("...")
                    time.sleep(3)
                    break

def go():
    input("Continue (Y/N)?")

def operations():
        number1 = eval(input("Enter a number: "))
        number2 = eval(input("Enter a second number: "))
        answer1 = number1 + number2
        answer2 = number1 - number2
        answer3 = number1 * number2
        answer4 = number1 / number2
        answer5 = number1 ** number2
        answer6 = number1 // number2
        answer7 = number1 % number2
        print("     [#1] Add")
        print("     [#2] Subtract")
        print("     [#3] Multiply")
        print("     [#4] Divide")
        print("     [#5] Floor Divide")
        print("     [#6] Exponent")
        print("     [#7] Modulo")
        ope = int(input("What do you want to do with the two numbers? (Enter just the number)\n"))
        if ope == 1:
            print("The sum of" , number1 , "and" , number2 , "is" , answer1)
        elif ope == 2:
            print("The difference of" , number1 , "and" , number2 , "is" , answer2)
        elif ope == 3:
            print("The product of" , number1 , "and" , number2 , "is" , answer3)
        elif ope == 4:
            print("The quotient of" , number1 , "and" , number2 , "is" , answer4)
        elif ope == 6:
            print(number1 , "exponent by" , number2 , "is" , answer5)
        elif ope == 5:
            print("The floor division of" , number1 , "and" , number2 , "is" , answer6)
        elif ope == 7:
            print("The remainder of" , number1 , "and" , number2 , "is" , answer7)
        else:
            print('INVALID INPUT. PLEASE TRY AGAIN')

def Initialize():
    os.system('cls')
    print("Initializing.")
    time.sleep(1)
    os.system('cls')
    print("Initializing..")
    time.sleep(1)
    os.system('cls')
    print("Initializing...")
    time.sleep(1)
    os.system('cls')

def LoadingScreen_Long():
    # Clear screen and start loading process
    os.system('cls')
    time.sleep(1)

    # First loading step
    print("\t\t\t\t\t\t\t\tLoading.")
    print('\t\t\t\t\t\t\t█')
    time.sleep(1)

    # Clear screen for the second loading step
    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading..")
    print('\t\t\t\t\t\t\t█████')
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading...")
    print('\t\t\t\t\t\t\t███████████')
    print('\t\t\t\t\t\t\t     Hang in there!')
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading.")
    print('\t\t\t\t\t\t\t███████████████')
    print('\t\t\t\t\t\t\t     Hang in there!')
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading..")
    print('\t\t\t\t\t\t\t████████████████████')
    print('\t\t\t\t\t\t\t     Hang in there!')
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading...")
    print('\t\t\t\t\t\t\t████████████████████████')
    print('\t\t\t\t\t\t\t     Hang in there!')
    time.sleep(1) 

    os.system('cls')
    print("\t\t\t\t\t\t\t\t")
    print('\t\t\t\t\t\t\t     Program Ready!')

def LoadingScreen_Short():
    # Clear screen and start loading process
    os.system('cls')
    time.sleep(1)

    # First loading step
    print("\t\t\t\t\t\t\t\tLoading.")
    print('\t\t\t\t\t\t\t████')
    time.sleep(1)

    # Clear screen for the second loading step
    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading..")
    print('\t\t\t\t\t\t\t███████')
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading...")
    print('\t\t\t\t\t\t\t███████████████')
    print("\t\t\t\t\t\t\t   No man's an island!")
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading..")
    print('\t\t\t\t\t\t\t█████████████████████')
    print("\t\t\t\t\t\t\t   No man's an island!")
    time.sleep(1)  

    os.system('cls')
    print("\t\t\t\t\t\t\t\tLoading...")
    print('\t\t\t\t\t\t\t████████████████████████')
    print("\t\t\t\t\t\t\t   No man's an island!")
    time.sleep(1) 

    os.system('cls')
    print("\t\t\t\t\t\t\t\t")
    print('\t\t\t\t\t\t\t     Program Ready!')

#THIS IS WHERE THE PROGRAM TRULY STARTS
time.sleep(1) 
LoadingScreen_Long()
os.system('cls')
time.sleep(1)
print("Welcome!")
print(" ")
time.sleep(1)
print("This'll serve as my(James Miro R. Orte) compilation of works and")
time.sleep(2)
print("culmination of learnings throughout my 1st Semester at DLL!")
print(" ")
time.sleep(2)
print("So without further ado...")
time.sleep(1)
print("please enjoy browsing through all my work!")
time.sleep(2)
LoadingScreen_Short()

print("Let's start off with the basics!")
time.sleep(1.5)
while menu:
    os.system('cls')
    print("")
    print("")
    print("               █▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬█")
    print("               █========================▶ THE MENU ◀=========================█")
    print("               █▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬█")
    print("               █    [#1] Greet Yourself!         [#11] Triangle Mania!        █")
    print("               █    [#2] Easy-Peasy Biodata!     [#12] Easy-Peasy Biodata!    █")
    print("               █    [#3] Guess the Password!     [#13] Easy-Peasy Biodata!    █")
    print("               █    [#4] Convert C° to F°!       [#14] Easy-Peasy Biodata     █")
    print("               █    [#5] Assignment Operators!   [#15] Easy-Peasy Biodata!    █")
    print("               █    [#6] Gold Miner!             [#16] Easy-Peasy Biodata!    █")
    print("               █    [#7] Your Age Group!         [#17] Easy-Peasy Biodata!    █")
    print("               █    [#8] Scholarship Grant!      [#18] Easy-Peasy Biodata!    █")
    print("               █    [#9] Loops!                  [#19] Easy-Peasy Biodata!    █")
    print("               █    [#10] Factorials!            [#20] Easy-Peasy Biodata!    █")
    print("               █▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬█")
    choice = int(input("So, what would you like to try? (Enter just the 'number' to the corresponding task)\n"))
    if choice == 1:
        os.system('cls')
        time.sleep(1)
        Initialize()
        os.system('cls')
        print("Welcome! This project will greet any and all names you put in it!")
        time.sleep(2)
        print("")
        print("Why not give it a try?")
        time.sleep(1)
        name = input("Please enter a name! ---> ")

        print("Hi " + name,"!")
        time.sleep(2)
        print("")
        print("Pretty fun wasn't it?")
        time.sleep(1)
        print("")
        print("Now go back and try the other fun options!")
        balik()
        continue
    elif choice == 2:
        Initialize()
        os.system('cls')
        time.sleep(1)
        print("Welcome to your very own Biodata Maker! ")
        time.sleep(1)
        print("")
        print("Just fill in the information asked and it'll do it for you")
        time.sleep(1)
        print('')
        print("Neat, ain't it?")
        time.sleep(1)
        os.system('cls')
        full_name = input("Please enter your full name: ")
        gender = input("Please enter your gender: ")
        age = input("Please enter your age: ")
        Fname = input("Please enter your father's full name: ")
        Mname = input("Please enter your mother's maiden name: ")
        nationality = input("Enter you nationality: ")
        birthdate = input("Enter your date of birth: ")
        birthplace = input("Enter your place of birth: ")
        civil_status = input("Enter your civil status: ")
        religion = input("Enter you religion: ")
        skills = input("Enter your relevant skills: ")
        hobbies = input("Enter your hobbies: ")
        email_address = input("Please enter a valid e-mail address: ")
        mobile_no = input("Please enter your mobile number: ")
        print("Hi! I'm " , full_name , "\b.I am" , gender , "and I am" , age , "years old. My parents are" , Fname , "and" , Mname, "\b. I am" , nationality , "and was born on", birthdate , "at" , birthplace , "and am currently" , civil_status,"\b. My religion is" , religion , "and I am proficient in" , skills , "and not only that but I also like to do" , hobbies , "in my free time. If you have any more questions about me you can contact me through" , email_address , "or" , mobile_no , "\b, and that's all about me. Thank you!")
        time.sleep(1)
        print('')
        ilu = input("So, did you like it? (Y/N): ")
        print('')
        print("Cool, now go and try the others!")
        balik()
        continue
    elif choice == 3:
        Initialize()
        password = input("Please enter a password ----> ")
        if password.lower() == "secret066":
            print("May tama ka!")
            print("Enjoy your 30 minutes of free browsing with SMART Prepaid!")
            balik()
        elif password == "jamesorte":
            print("Well tama rin")
            print("Enjoy your 30 minutes of free browsing with SMART Prepaid!")
            balik()
        else:
            print("Nope, try again")
            print("Hint: First & Last name of author")
            balik()
        print("Thank you for choosing Globe, as your number one service provider!")
        time.sleep(2)
        continue
    elif choice == 4:
        Initialize()
        print("Farenheit to Celsius Converter Program!")
        time.sleep(1)

        fahrenheit = eval(input("Please enter temperature in Farenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print("The conversion of" , fahrenheit , "degrees Fahrenheit is" , round(celsius,2) , "degrees Celcius!")
        time.sleep(2)
        input("Get it? (Y/N)")
        continue
    elif choice == 5:
        x = 5
        Initialize()
        print("Welcome to a guide to ASSIGNMENT Operators!")
        time.sleep(1)
        print("")
        print("Let's say x = 5")
        print("")
        time.sleep(2)
        print("Then say we do: x = x + 10")
        x = x + 10
        time.sleep(2)
        print("We added 10 to x so our total would now amount to:", x)
        time.sleep(2)
        print("")
        print("Let's try adding another:")
        time.sleep(1)
        print("x = x + 15")
        x = x + 15
        time.sleep(2)
        print("")
        print("Our total would now amount to ", x)
        time.sleep(3)
        os.system('cls')
        print("By using these assignment operators")
        time.sleep(1)
        print("We can use these to do basic operations on numeric values")
        print('')
        time.sleep(1)
        print("                                            >List of Operations<")
        print("                                     █▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬█")
        print("                                     █   = - Assigns values            █")
        print("                                     █   + or += Adds two values       █")
        print("                                     █   - or -= Subtracts two values  █")
        print("                                     █   * or *= Multiplies two values █")
        print("                                     █   / or /= Divides two values    █")
        print("                                     █   // or //= Divides floor value █")
        print("                                     █   % or %= Gives the remainder   █")
        print("                                     █   ** or **= Raises exponent     █")
        print("                                     █▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬█")
        print("Have a go with it!")
        time.sleep(1)
        operations()
        print("")
        input("Easy, right? (Y/N): ")
    elif choice == 6:
        os.system('cls')
        Initialize()
        name = input("What's your name?: ")
        tot = 0
        ans = input(f"So {name},have you mined today? (Y/N):  ")
        print("\n")
        if ans.upper() == "Y": #main operation if "yes"
            gold = eval(input("How much Gold did you mine (Number)? "))
            all = tot + gold
            print(f"Good day {name}, you have mined {all} gold today!")
            time.sleep(2)
        elif ans.upper() != "Y": #sub operation if "no"
            print("Then go mine some", name )
            time.sleep(2)
        else:
            print("Huh?")
            time.sleep(2)
        pass
    elif choice == 7:
        Initialize()
        print("Find out your age with a press of a button!")
        age = eval(input("Please enter your age: "))
        if age >= 1 and age <= 7:
            print("You're a toddler")
            input("Go back (Y/N)? ")
        elif age >= 8 and age<= 13:
            print("You're a preteen")
            input("Go back (Y/N)? ")
        elif age >= 14 and age<= 18:
            print("You're a teenager")
            input("Go back (Y/N)? ")
        elif age >= 19 and age<= 31:
            print("You're an early adult")
            input("Go back (Y/N)? ")
        elif age >= 32 and age<= 45:
            print("You're a mid adult")
            input("Go back (Y/N)? ")
        elif age >= 46 and age<= 59:
            print("You're a post adult")
            input("Go back (Y/N)? ")
        elif age >= 60 and age <= 100:
            print("You're a senior ")
            input("Go back (Y/N)?")
        else:
            print("Tanda mo naman")
            input("Go back (Y/N)? ")
       
    elif choice == 8:
        Initialize()
        isDLL = input("Are you currently enrolled ni DLL?(Y/N): ")
        if isDLL.lower() == "y":
            isIYAM = input("Do you currently live in Brgy. Ibabang Iyam?(Y/N): ")
            if isIYAM.lower() == "y":
                print("Welcome! Please confirm your school year")
                print("F - Freshman")
                print("S - Sophomore")
                print("J - Junior")
                print("R - Senior")
                isSY = input("Please enter your current year level in DLL:")
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
                        balik()
                    else:
                        print("Okay, have a nice day")
                        balik()
            else:
                print("Sorry, you are not eligible")
                balik()
        else:
            print("Sorry, you are not eligible")
            balik()
    elif choice == 9:
        Initialize()
        print("Welcome to loops! Using the loop function")
        print("we can repeat a code block as many times we want")
        time.sleep(1)
        print()
        print("It should look like this:")
        print("for x in range(Starting_Point,Stopping_Point, Increment/Decrement):")
        go()
        print('')
        print("So let's say:")
        print("for x in range(1,11):")
        print("     print(""Hello World"")")
        go()
        os.system('cls')
        print("It should look like this:")
        time.sleep(1)
        for x in range(1,11):
            print("     Hello World")
        time.sleep(1)
        print('Neat!')
        balik()
    elif choice == 10:
        Initialize()
        print("Welcome. You can factorial any number here!")
        factorial = 1
        print("")
        start = eval(input("So, enter the number you want to factorial: "))
        for x in range(start,0,-1):
            print(x)
            factorial *= x
            print(f"the factorial of {start} is {factorial} ")
        time.sleep(1)
        print("Neat")
        balik()
    elif choice == 11:
        for x in range(0,11):
        print(x, end = " ")
        for y in range(0,11):
            print(" *", end ="")
        print()
        pass
    elif choice == 12:
        pass
    elif choice == 13:
        pass
    elif choice == 14:
        pass
    elif choice == 15:
        pass
    elif choice == 16:
        pass
    elif choice == 17:
        pass


    else:
        print("None of the options were chosen. TERMINATING PROGRAM")
        break
