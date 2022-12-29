# Check whether the given number is Armstrong number or not
# armstrong number is 1.counting the number of digits 2. raising each number to the count

import math
num=int(input()) #to input a number
n=num
n2=num
c=0

while(n!=0): #loop to count number of digits
    c+=1
    n//=10

sum=0
while(n2!=0):
    sum=sum+pow((n2%10),c)
    n2//=10

if sum==num:
    print("armstrong")
else:
    print("not armstrong")


