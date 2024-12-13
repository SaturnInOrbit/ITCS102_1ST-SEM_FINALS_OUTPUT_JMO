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