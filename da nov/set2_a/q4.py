# Write a program in python to solve a quadratic equation. 
import math
a=int(input("Enter the coeff of x^2 \n"))
b=int(input("Enter the coeff of x \n"))
c=int(input("Enter the value of constant \n"))
x1= (-b+math.sqrt(b*b-4*a*c))/(2*a)
x2= (-b-math.sqrt(b*b-4*a*c))/(2*a)
print("The roots of the given quadratic are: ",x1," and ",x2)
