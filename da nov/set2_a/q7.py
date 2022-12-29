# Write a program in python to swap two numbers using tuple assignment
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
print("Values before swap ")
print ("a=",a, "b=",b)
(a,b)=(b,a)
print("Values after swap ")
print("a=",a, "b=",b)