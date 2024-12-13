import os


tria = 1
tuloy = True
while tuloy == True:
    triangle = input("Would you like to add a triangle?(Y/N): ")
    if triangle.lower() == "n":
        print("OKAY SIGE TAMA NA")
        break
    else:
        os.system = 'cls'
        tria += 1
        for x in range (1,5):
            for r in range(1,tria+1):
                for y in range(1,x+1):
                    print("* ", end ="")
                for z in range(5,x,-1):
                    print(" ",end=" ")
            print()
        continue