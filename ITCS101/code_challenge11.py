for x in range(5, 0, -1):
    for y in range(1, x + 1):
        print(" ", end=" ")
    for z in range(5, x, -1):
        print("*", end=" ")
    for a in range(4, x, -1):
        print("*", end=" ")
    print()


for x in range(1, 5):
    for y in range(1, x + 2):
        print(" ", end=" ")
    for z in range(4, x, -1):
        print("*", end=" ")
    for a in range(3, x, -1):
        print("*", end=" ")
    print()