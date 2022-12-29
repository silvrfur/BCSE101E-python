# Write a program in python to input three sides of a triangle and check whether the triangle is equilateral, isosceles or scalene
a=int(input("Enter the first side of triangle \n"))
b=int(input("Enter the second side of triangle \n"))
c=int(input("Enter the third side of triangle \n"))

if a==b and b==c and a==c:
    print("equilateral triangle")
elif a!=b and b!=c and c!=a:
    print("scalene traingle")
else:
    print("isosceles triangle")