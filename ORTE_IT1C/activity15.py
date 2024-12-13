for x in range(0,10):
    print(x, end=" ")
    for y in range(0,x):
        print(" *", end ="")
    print()
for x in range(10,-1,-1):
    print(x, end = " ")
    for y in range(x,0,-1):
        print(" *", end ="")
    print()