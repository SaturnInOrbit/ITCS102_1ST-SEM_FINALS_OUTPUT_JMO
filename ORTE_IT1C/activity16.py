def upsidedown_tria():
    t = int(input("Enter a number range: "))
    #arrow down
    for x in range(1,t):
        #left right angle triangle = space
        for a in range(1,x,1):
            print(" ",end="  ")
        #inverted right triangle = up arrow
        for b in range(t,x,-1):
            print("^ ",end=" ")
        #left right angle triangle = asterisk    
        for b in range(t,x,-1):
            print("* ",end=" ")        
        print()   
upsidedown_tria()