#pat 1 batch 2 9 dec
'''
Write a Python program using while loop to get numbers until -1 is encountered. Find the count of the Amstrong Numbers present in the given set of numbers and display the count for both the cases.

Input : Get numbers from the user separated by a space until -1 is encountered.

Output: Display the "AmstrongCount" and the "NonAmstrongCount" using the respective variable names specified.

Test case1

1
153
155
9
-1

Output:

AmstrongCount is 3
NonAmstrongCount is 1



Testcase2:

Input:

0
9474
370
371
300
-1

Output:

AmstrongCount is 4
NonAmstrongCount is 1
'''
'''
count the number of digits, raise the digits to that count
'''
import math
a,na=0,0
while True:
    sum=0
    n=int(input())
    if n==-1:
        break
    c=len(str(n))
    num=n
    while n!=0:
        sum=sum+math.pow((n%10),c)
        n//=10
    if sum==num:
        a+=1
    else:
        na+=1
print("AmstorngCount is ",a)
print("NonAmstorngCount is ",na)