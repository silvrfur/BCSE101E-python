# Take integer inputs from user until he/she presses q (Ask to press q to quit after every integer input ). Print average and product of all numbers. 

sum=0
product=1
c=0
while True:
    num=input()
    if num=='q':
        break
    num=int(num)
    sum=sum+num
    product=product*num
    c+=1
avg=sum/c
print("The avg= ",avg)
print("The product= ",product)
