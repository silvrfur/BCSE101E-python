# Read a number, check if it is positive, negative or zero. Increment the number if it is positive, decrement if it is negative. (elif statement) 
n=int(input("Enter the number \n"))
if n>=0:
    n+=1
else:
    n-=1
print("Number after update is: ",n)