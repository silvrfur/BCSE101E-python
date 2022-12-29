'''
Write a Python program to find numbers between 1 and 400 (both included) 
where each digit of a number is an even number. 
The numbers obtained should be stored in a list and displayed
'''

myList=[]
for i in range(1,401):
    flag=False #it assumes that all the digits are odd
    n=i
    while(n!=0):
        d=n%10
        if(d%2==0):
            flag=True
        else:
            flag=False
            break
        n//=10
    if(flag==True):
        # print(i)
       myList.append(i)
print(myList)