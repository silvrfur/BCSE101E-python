#pat 1 batch 1 9dec
'''
Write a Python program using while loop to read the numbers until -1 is encountered. Count the number of prime and composite numbers entered by the user. 

Input: Numbers are given one after the other in separate lines. Give the last number as -1. 

Output: Print the count of the prime numbers using the variable name PrimeCount and the count of composite numbers using the variable name CompositeCount.

Test case:

4
6
7
8
9
10
11
35
76
39
-1

Output:

primecount is 2
compositecount is 8

'''
def prime(n):
    flag=True
    for i in range(2,n):
        if n%i==0:
            flag=False
            break
    if flag:
        return True
    else:
        return False

cp,cc=0,0
while True:
    n=int(input())
    if n==-1:
        break
    if prime(n):
        cp+=1
    else:
        cc+=1
print("primecount is ",cp)
print("compositecount is ",cc)