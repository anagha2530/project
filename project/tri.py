print("enter the sides of triangle")
side1 = float(input("enter the side1: "))
side2 = float(input("enter the side2: "))
side3 = float(input("enter the side3: "))
if (side1+side2>side3 and side2+side3>side1 and side1+side3>side2):
    if(side1 == side2 == side3):
        print("equilateral triangle")
    elif(side1 == side2 or side2 == side3 or side3 == side1):
        print("isocelous triangle")
    
    else:
        print("scalar")
else:
    print("invalid")