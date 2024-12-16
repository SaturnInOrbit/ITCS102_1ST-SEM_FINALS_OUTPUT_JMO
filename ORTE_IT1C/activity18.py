def ine_triangle():
    tria = eval(input("Enter how many triangles you want: "))
    for x in range (1,6):
        for r in range(1,tria+1):
            for y in range(1,x+1):
                print("* ", end ="")
            for z in range(5,x,-1):
                print(" ",end=" ")
        print()