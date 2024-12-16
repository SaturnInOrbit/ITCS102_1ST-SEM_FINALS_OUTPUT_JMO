def mine():
    name = input("What's your name?: ")
    tot = 0
    ans = input("Have you mined today? (Y/N)  ")
    print("\n")

    if ans.upper() == "Y": #main operation if "yes"
        gold = eval(input("How much Gold did you mine? "))
        all = tot + gold
        print("Good day ",name,"You have mined ", all," golds, today")
    elif ans.upper() != "Y": #sub operation if "no"
        print("The go mine some", name )
    else:
        print("Huh?")