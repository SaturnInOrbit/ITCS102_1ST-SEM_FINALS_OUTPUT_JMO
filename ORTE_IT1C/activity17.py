def multi_table():
    colu = eval(input("Enter how many tables you want: "))
    for x in range (1,11):
        for y in range(1,colu+1):
            print(f"{x} x {y} = {x*y}", end ="\t")
        print()