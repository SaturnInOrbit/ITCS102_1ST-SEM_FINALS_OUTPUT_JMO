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
    time.sleep(1)
    os.system('cls')
    print("Initilaizing.")
    time.sleep(1)

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
# time.sleep(2)
# print("This'll serve as my(James Miro R. Orte) compilation of works and")
# time.sleep(3)
# print("culmination of learnings throughout my 1st Semester at DLL!")
# print(" ")
# time.sleep(3)
# print("So without further ado...")
# time.sleep(2)
# print("please enjoy browsing through all my work!")
# time.sleep(3)
# LoadingScreen_Short()

print("Let's start off with the basics!")
time.sleep(2)
for x in range(1,2):
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
        import activity2
    else:
        print("None of the options were chosen. TERMINATING PROGRAM")
        break
