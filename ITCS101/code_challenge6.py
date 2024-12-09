prelim = eval(input("Enter your prelim grade: "))
midterm = eval(input("Enter your midterm grade: "))
sfinals = eval(input("Enter your semifinal grade: "))
final = eval(input("Enter your finals grade: "))
quiz = eval(input("Enter your quizzes grade: "))
project = eval(input("Enter your projects grade: "))

if (prelim >= 65 and prelim <=100) and (midterm >= 65 and midterm <=100) and (sfinals >=65 and sfinals <=100): 
	FG = prelim * 0.15 + midterm * 0.15 + sfinals * 0.15 + final * 0.15 + quiz * 0.25 + project * 0.15
	
	if FG > 75:
		print("Congratulations, you passed the course/subject") 
	else: 
		print("Sorry, you failed") 
else:
	print("INVALID GRADE")
