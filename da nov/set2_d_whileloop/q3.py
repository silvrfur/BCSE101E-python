# Write a program in python to print the sum of all the digits of a number
num=int(input("Enter the number \n"))
sum=0
while(num!=0):
    sum+=(num%10)
    num/=10
print("The sum of numbers: ",sum)