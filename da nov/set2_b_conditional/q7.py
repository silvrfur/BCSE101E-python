# Create a simple calculator. (elif statement) 
print('''
        Enter 1, to add
        Enter 2, to subtract
        Enter 3, to multiply
        Enter 4, to divide
        ''')
ch=int(input("Enter your choice \n"))
a=int(input("Enter first number \n"))
b=int(input("Enter second number \n"))
if ch==1:
    print("Sum is ",(a+b))
elif ch==2:
    print("Diffrence is",(a-b))
elif ch==3:
    print("Product is ",(a*b))
else:
    print("Quotient is ",(a/b))