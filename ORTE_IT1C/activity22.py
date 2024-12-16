go = True
names_list = []

while go:
    name = input("Enter a name (Enter 'stop' to stop): ")
    if name.lower() == "stop":
        print(f"Here's your list of names : {names_list}")
        print(f"You have entered {len(names_list)} names!")
        break
    else:
        names_list.append(name)