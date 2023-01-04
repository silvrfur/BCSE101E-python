# pat 1 batch 1
'''
Write a Python Code to check whether the number that is given by the user is a STRONG number or not.
Continue getting the numbers till -1 is pressed by the user. Display the count of both the cases.

Input: Get values one after the other from the user till the user enters -1.

Output: Display the count of STRONG and NOT_STRONG numbers



Test case 1:

1
3
5
10
145
-1

Output:

STRONG_NUMBERS_COUNT is 2
NON_STRONG_NUMBERS_COUNT is 3

Test case 2:

1
2
145
40585
-1

Output:

STRONG_NUMBERS_COUNT is 4
NON_STRONG_NUMBERS_COUNT is 0
'''

'''
143=1!+4!=3!
'''
s=0
ns=0

def fact(n): #function to calculate factorial of a number
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

# ans=fact(4)
# print(type(ans))
while True:
    sum=0
    n=int(input())
    if n==-1:
        break
    num=n
    while n!=0: #loop for extraction of digits
        d=n%10
        f=fact(d)
        n//=10
        sum=sum+fact(d)
    if num==sum:
        s+=1
    else:
        ns+=1
    
print("STRONG_NUMBERS_COUNT is ",s)
print("NON_STRONG_NUMBERS_COUNT is ",ns)