tuloy = True
nameno = 0
while tuloy == True:
    name = input("Enter a name: ")

    if name.lower()=="stop":
        print("Okay tama na")
        print(f"You have entered a total of {nameno} names!")
        break

    else:
        nameno += 1
        continue