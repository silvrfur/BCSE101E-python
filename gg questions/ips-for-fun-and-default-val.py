#ips for fun and default values 9 dec
'''
Given the number of hours and minutes browsed, write a program using functions to calculate bills for Internet Browsing in a browsing centre. The conditions are given below.
(a) 1 Hour - Rs.50
(b) 1 minute - Re. 1
(c) Five hours - Rs. 200
Pass the number of hours and minutes browsed to the function and display the result in the driver program from where the function was called.

Use default values in case the number of hours or minutes are not being passed.

Test case1:
Input:
5
10
Output
210

Test case2:
Input:
6
21
Output:
271

'''
def bill(hrs,min):
    amt=(hrs//5)*200+(hrs%5)*50+min
    return amt
hrs=int(input())
min=int(input())
print(bill(hrs,min))