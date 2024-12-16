import os
import time
menu = True

def Initialize():
    print("Initilaizing.")
    time.sleep(1)
    os.system('cls')
    print("Initilaizing..")
    time.sleep(1)
    os.system('cls')
    print("Initilaizing...")


# def LoadingScreen_Long():
#     # Clear screen and start loading process
#     os.system('cls')
#     time.sleep(1)

#     # First loading step
#     print("\t\t\t\t\t\t\t\tLoading.")
#     print('\t\t\t\t\t\t\t█')
#     time.sleep(1)

#     # Clear screen for the second loading step
#     os.system('cls')
#     print("\t\t\t\t\t\t\t\tLoading..")
#     print('\t\t\t\t\t\t\t█████')
#     time.sleep(1)  

#     os.system('cls')
#     print("\t\t\t\t\t\t\t\tLoading...")
#     print('\t\t\t\t\t\t\t███████████')
#     print('\t\t\t\t\t\t\t     Hang in there!')
#     time.sleep(1)  

#     os.system('cls')
#     print("\t\t\t\t\t\t\t\tLoading.")
#     print('\t\t\t\t\t\t\t███████████████')
#     print('\t\t\t\t\t\t\t     Hang in there!')
#     time.sleep(1)  

#     os.system('cls')
#     print("\t\t\t\t\t\t\t\tLoading..")
#     print('\t\t\t\t\t\t\t████████████████████')
#     print('\t\t\t\t\t\t\t     Hang in there!')
#     time.sleep(1)  

#     os.system('cls')
#     print("\t\t\t\t\t\t\t\tLoading...")
#     print('\t\t\t\t\t\t\t████████████████████████')
#     print('\t\t\t\t\t\t\t     Hang in there!')
#     time.sleep(1) 

#     os.system('cls')
#     print("\t\t\t\t\t\t\t\t")
#     print('\t\t\t\t\t\t\t     Program Ready!')

# def LoadingScreen_Short():
#     # Clear screen and start loading process
#     os.system('cls')
#     time.sleep(1)

#     # First loading step
#     print("\t\t\t\t\t\t\t\tLoading.")
#     print('\t\t\t\t\t\t\t████')
#     time.sleep(1)

#     # Clear screen for the second loading step
#     os.system('cls')
#     print("\t\t\t\t\t\t\t\tLoading..")
#     print('\t\t\t\t\t\t\t███████')
#     time.sleep(1)  

#     os.system('cls')
#     print("\t\t\t\t\t\t\t\tLoading...")
#     print('\t\t\t\t\t\t\t███████████████')
#     print("\t\t\t\t\t\t\t   No man's an island!")
#     time.sleep(1)  

#     os.system('cls')
#     print("\t\t\t\t\t\t\t\tLoading..")
#     print('\t\t\t\t\t\t\t█████████████████████')
#     print("\t\t\t\t\t\t\t   No man's an island!")
#     time.sleep(1)  

#     os.system('cls')
#     print("\t\t\t\t\t\t\t\tLoading...")
#     print('\t\t\t\t\t\t\t████████████████████████')
#     print("\t\t\t\t\t\t\t   No man's an island!")
#     time.sleep(1) 

#     os.system('cls')
#     print("\t\t\t\t\t\t\t\t")
#     print('\t\t\t\t\t\t\t     Program Ready!')

# #THIS IS WHERE THE PROGRAM TRULY STARTS
# time.sleep(1) 
# LoadingScreen_Long()
# os.system('cls')
# time.sleep(1)
# print("Welcome!")
# print(" ")
# time.sleep(1)
# print("This'll serve as my(James Miro R. Orte) compilation of works and")
# time.sleep(2)
# print("culmination of learnings throughout my 1st Semester at DLL!")
# print(" ")
# time.sleep(2)
# print("So without further ado...")
# time.sleep(1)
# print("please enjoy browsing through all my work!")
# time.sleep(2)
# LoadingScreen_Short()

print("Let's start off with the basics!")
time.sleep(1.5)
while menu:
    os.system('cls')
    print("")
    print("")
    print("                                     █▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬█")
    print("                                     █==========▶ THE MENU ◀===========█")
    print("                                     █▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬█")
    print("                                     █    [#1] Greet Yourself!         █")
    print("                                     █    [#2] Easy-Peasy Biodata!     █")
    print("                                     █    [#3] Sum of TWO inputs       █")
    print("                                     █    [#4] Convert C° to F°!       █")
    print("                                     █    [#5] Assignment Operators!   █")
    print("                                     █    [#6] Conditional Statements! █")
    print("                                     █    [#7] Your Age Group!         █")
    print("                                     █    [#8] Scholarship Grant!      █")
    print("                                     █    [#9] Loops!                  █")
    print("                                     █    [#10] Factorials!            █")
    print("                                     █▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬█")
    choice = int(input("So, what would you like to try? (Enter just the 'number' to the corresponding task)\n"))
    if choice == 1:
        os.system('cls')
        time.sleep(1)
        Initialize()
        time.sleep(2)
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
        time.sleep(1)
        continue
    elif choice == 2:
        Initialize
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
        time.sleep(1)
        continue
    elif choice == 3:
        Initialize()
        print("Welcome to the adding machine!")
        time.sleep(1)
        print("This is where you can add two numbers together")
        time.sleep(1)
        print("Try it!")
        time.sleep(1)
        print("")
        number1 = eval(input("Enter a number: "))
        number2 = eval(input("Enter a second number: "))
        answer = number1 + number2
        print("The sum of" , number1 , "and" , number2 , "is" , answer)
        time.sleep(1)
        print('')
        print("Now you can add any two digits you want!")
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
        pass
    elif choice == 5:
        x = 5
        Initialize()
        print("Welcome to guide to ASSIGNMENT Operators!")
        time.sleep(1)
        print("")
        print("Let's say x = 5")
        print("x = 5")                                                                 

        print(x)
        x = x + 10
        x = x + 10

        print(x)

        x = x + 15

        print(x)

        x += 20
        print(x)

        x -= 25
        print(x)
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        pass
    elif choice == 8:
        pass
    elif choice == 9:
        pass
    elif choice == 10:
        pass

    else:
        print("None of the options were chosen. TERMINATING PROGRAM")
        break
