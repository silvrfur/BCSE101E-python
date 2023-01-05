# ips for recursive functions
'''
Q. 
Write Python code to find the factorial of a  number n using a recursive function named "fact(n)". Return the value at the end of the function.

Here pass the value of n from the driver code which will be a function named "Sum_Series_fact(n)".

That is, Call this function fact(n)  in another recursive function named "Sum_Series_fact(n)".

In Sum_Series_fact(n) the value of n means the maximum number of factorial terms to be calculated and summed up to find the total of all factorials starting from fact(0).

For example if the input for Sum_Series_fact(n) is 5, then find fact(0), fact(1), fact(2), fact(3) and fact(4). Total all the values and display the result.
'''

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
    

def Sum_Series_fact(n):
    if n==0:
        return 0
    # print(fact(n-1))
    return fact(n-1)+Sum_Series_fact(n-1)

N=int(input())
print(Sum_Series_fact(N))

#ips for recursive function ---sum of multiples of 3 till that given number using recursion
#tower of hanoi