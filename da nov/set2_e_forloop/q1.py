# Write a Python program to construct the following pattern, using a nested for loop.
'''
a.
*
**
***
****
*****
****
***
**
*
''' 
for i in range(1,10):
    if i<=5:
        print("*"*i)
    else:
        print("*"*(5-(i-5)))

'''
b.
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1
'''
for i in range(1,6):
    for j in reversed(range(1,i+1)):
        print(j),
    print()
    