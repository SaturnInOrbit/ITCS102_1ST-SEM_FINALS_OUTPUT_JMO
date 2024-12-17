tuloy = True
total = 0
while tuloy == True:
    num = eval(input("Enter a number: (Press '0' to stop): "))

    if num == 0:
        print("Okay tama na")
        print(f"The total of your inputted numbers is {total}!")
        break

    else:
        total += num
        continue