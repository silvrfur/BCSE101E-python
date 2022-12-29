# Find the largest of 3 numbers. (elif statement)
a=int(input("Enter the first number \n"))
b=int(input("Enter the second number \n"))
c=int(input("Enter the third number \n"))

if a>b and a>c:
    print(a," is largest")
elif b>c and b>a:
    print(b, " is largest")
else:
    print(c," is largest")