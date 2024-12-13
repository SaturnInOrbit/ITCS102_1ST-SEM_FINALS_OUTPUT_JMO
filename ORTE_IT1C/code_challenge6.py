prelim = int(input("Enter your score for the prelims: "))
midterm = int(input("Enter your score for the midterms: "))
semif = int(input("Enter your score for the semifinals: "))
final = int(input("Enter your score for the finals: "))
quiz  = int(input("Enter your score for the quizzes: "))
project = int(input("Enter your score for the projects: "))

FG = prelim * 0.15 + midterm * 0.15 + semif * 0.15 + final * 0.15 + quiz * 0.25 + project * 0.15 
print("Your Final Grade issssss" , FG)
if FG > 100:
	print("Aw you cheated, fail")
	print("Kaya mo yan")
elif FG >= 75:
	print("Pasado ka! Yey!")
	print("Keep it up")
else:
	print("Welp, only way is up from here")

print("good luck, keep it up!")