# Write a program in python to input three sides of a triangle and check whether it is right angled one
import math
h=int(input("Enter the height of the triangle \n"))
b=int(input("Enter the base of the triangle \n"))
hyp=int(input("Enter the hypoteneous of the triangle \n"))

if (math.pow(b,2)+math.pow(h,2))==math.pow(hyp,2):
    print("is a right angled triangle")
else:
    print("not a right angled traingle")