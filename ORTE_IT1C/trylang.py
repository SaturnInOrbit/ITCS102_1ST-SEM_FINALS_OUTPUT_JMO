menu = True
        number1 = eval(input("Enter a number: "))
        number2 = eval(input("Enter a second number: "))
        answer1 = number1 + number2
        answer2 = number1 - number2
        answer3 = number1 * number2
        answer4 = number1 / number2
        answer5 = number1 ** number2
        answer6 = number1 // number2
        answer7 = number1 % number2
        print("     [#1] Add")
        print("     [#2] Subtract")
        print("     [#3] Multiply")
        print("     [#4] Divide")
        print("     [#5] Floor Divide")
        print("     [#6] Exponent")
        print("     [#7] Modulo")
        ope = print("What do you want to do with the two numbers? (Enter just the number)")
        if ope == 1:
            print("The sum of" , number1 , "and" , number2 , "is" , answer1)
        elif ope == 2:
            print("The difference of" , number1 , "and" , number2 , "is" , answer2)
        elif ope == 3:
            print("The product of" , number1 , "and" , number2 , "is" , answer3)
        elif ope == 4:
            print("The quotient of" , number1 , "and" , number2 , "is" , answer4)
        elif ope == 6:
            print(number1 , "exponent by" , number2 , "is" , answer5)
        elif ope == 5:
            print("The floor division of" , number1 , "and" , number2 , "is" , answer6)
        elif ope == 7:
            print("The remainder of" , number1 , "and" , number2 , "is" , answer7)
        else:
            print('INVALID INPUT. PLEASE TRY AGAIN')