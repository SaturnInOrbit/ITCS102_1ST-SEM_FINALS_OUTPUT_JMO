AA = input("What's your name, miner? ")
print("\n")
A = 0
B = input("Have you mined today?  ")
print("\n")



if B.upper() == "YES": #main operation if "yes"
	C = eval(input("How many  Golds did you mined? "))
	print("\n")
	D = A + C
	print("Congrats ",AA,"You have mined ", D," golds, today")
elif B.upper() != "YES": #sub operation if "no"
	print("\n")
	print("That's unfortunate, ",AA, " you've mined ", A, " golds today" )
	print(" you should mine more efficient ", AA)