def num_triangle():
    for x in range(0,10):
        print(x, end=" ")
        for y in range(0,x):
            print(" *", end ="")
        print()