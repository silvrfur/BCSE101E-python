'''
Write a Python code to display all the happy numbers in a list data structure from 0 till the given number N which is got as input

Input: Getthe value of N from the user

Output: Display all the Happy Numbers in a list from 0 till that number N



Test case 1:

Input:

100

Output:

[1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]



Test case 2:

Input:

7

Output:

[1, 7]
'''

import math
def happy(n):
    sum=0
    flag=False
    
    while n>1:
        # print("the number is",n)
        while n!=0:
            sum=sum+int(math.pow((n%10),2))
            n//=10
        # print("the sum is",sum)
        n=sum
        sum=0
        if n==1:
            flag=True 
            break
        if n>1 and n<=9:
            break
    if flag==True:
        return True
        # print("happy number")
    else:
        return False
        # print("not happy")
        


num=int(input())
lst=[1]
for i in range(2,num+1):
    if happy(i)==True:
        lst.append(i)
print(lst)




